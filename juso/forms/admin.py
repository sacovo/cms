import csv
from datetime import datetime

import xlsxwriter

from content_editor.admin import ContentEditor, ContentEditorInline
from django.contrib import admin, messages
from django.db import models
from django import forms
from django.http import HttpResponse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from reversion.admin import VersionAdmin
from flat_json_widget.widgets import FlatJsonWidget

# Register your models here.

from juso.forms.models import Form, FormField, MailchimpConnection
from juso.sections.models import Section
from juso.utils import CopyContentMixin


class FormFieldInline(ContentEditorInline):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("name", "slug", "input_type", "required"),
                    "ordering",
                    "region",
                )
            },
        ),
        (
            _("advanced"),
            {
                "classes": ("collapse",),
                "fields": (
                    "size",
                    "choices",
                    "initial",
                    "help_text",
                    "unique",
                    "unique_error",
                ),
            },
        ),
    )


@admin.register(Form)
class FormAdmin(VersionAdmin, ContentEditor, CopyContentMixin):
    list_display = [
        "title",
        "slug",
        "created_date",
        "section",
        "language_code",
        "count",
    ]

    list_filter = [
        "section",
        "language_code",
    ]

    autocomplete_fields = ["section", "mailchimp_connection"]

    search_fields = [
        "title",
    ]

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_date",
        "edited_date",
    )

    formfield_overrides = {
        models.JSONField: {'widget': FlatJsonWidget},
    }

    fieldsets = (
        (
            None,
            {"fields": ("title", "slug", "section", "created_date", "edited_date",)},
        ),
        (
            _("settings"),
            {
                "classes": ("tabbed",),
                "fields": (
                    "submit",
                    "size",
                    "success_message",
                    "success_redirect",
                    "fullwidth",
                ),
            },
        ),
        (
            _("collection"),
            {
                "classes": ('tabbed',),
                "fields": (
                    "email",
                    "list_id",
                    "webhook",
                    "mailchimp_connection",
                    "mailchimp_list_id",
                    "webhook_dict",
                )
            }
        ),
        (
            _("meta"),
            {
                "classes": ("tabbed",),
                "fields": (
                    "meta_title",
                    "meta_author",
                    "meta_description",
                    "meta_image",
                    "meta_image_ppoi",
                    "meta_robots",
                    "meta_canonical",
                ),
            },
        ),
    )

    actions = ["export_form", "clear_form", "export_form_xlsx"]

    inlines = [
        FormFieldInline.create(FormField),
    ]

    plugins = [FormField]

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)

        if obj is None or request.user.is_superuser:
            return super().get_fieldsets(request, obj=obj)

        sections = request.user.section_set.all()
        if obj.section in sections:
            return super().get_fieldsets(request, obj=obj)
        return (
            (
                None,
                {"fields": ("title", "slug", "section", "created_date", "edited_date",)},
            ),
        )


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)


        if "section" not in form.base_fields:
            return form

        section_field = form.base_fields["section"]
        form.base_fields['list_id'].widget = forms.PasswordInput()

        sections = request.user.section_set.all()
        section_field.initial = sections[0]

        return form

    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return super().has_change_permission(request, obj)
        sections = request.user.section_set.all()
        return obj.section in sections

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return super().has_change_permission(request, obj)
        sections = request.user.section_set.all()
        return obj.section in sections

    def can_access_entries(self, form, request):
        if form.section not in Section.objects.filter(users=request.user):
            messages.add_message(request, messages.ERROR, _("access denied"))
            return False
        return True


    def export_form(self, request, query):

        form = query.first()

        if not self.can_access_entries(form, request):
            return

        entries, fields = form.entry_dict()

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{form.slug}-{timezone.now():%Y%m%d%H%M}.csv"'

        writer = csv.DictWriter(response, fieldnames=fields)
        writer.writeheader()
        writer.writerows(entries)

        return response

    def export_form_xlsx(self, request, query):
        form = query.first()

        if not self.can_access_entries(form, request):
            return

        entries, fields = form.entry_dict()

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = f'attachment; filename="{form.slug}-{timezone.now():%Y%m%d%H%M}.xlsx"'

        workbook = xlsxwriter.Workbook(response, {'remove_timezone': True})
        worksheet = workbook.add_worksheet('answers')
        bold = workbook.add_format({'bold': True})
        date_format = workbook.add_format({'num_format': 'yy-mm-dd hh:mm'})

        for col, field in enumerate(fields):
            worksheet.write(0, col, field, bold)

        for row, entry in enumerate(entries):
            for col, field in enumerate(fields):
                val = entry.get(field, '')
                if isinstance(val, datetime):
                    worksheet.write(row + 1, col, entry.get(field, ''), date_format)
                else:
                    worksheet.write(row + 1, col, entry.get(field, ''))

        workbook.close()

        return response


    def clear_form(self, request, query):
        form = query.first()
        response = self.export_form_xlsx(request, query)

        if response:
            form.clear_entries()

        return response


@admin.register(MailchimpConnection)
class MailchimpConnectionAdmin(admin.ModelAdmin):

    list_display = (
        "name", "section", "api_server"
    )

    search_fields = (
        "name", "section"
    )

    autocomplete_fields = (
        "section",
    )

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        sections = request.user.section_set.all()
        return super().get_queryset(request).filter(section__in=sections)
