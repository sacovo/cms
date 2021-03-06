# Generated by Django 3.0.5 on 2020-05-23 15:48

import uuid

import django.db.models.deletion
import django.utils.timezone
import imagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0018_auto_20200509_1826"),
        ("people", "0011_auto_20200508_2342"),
        ("sections", "0009_auto_20200507_1758"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0034_auto_20200523_1748"),
        ("events", "0034_auto_20200510_1938"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="articleplugin",
            options={
                "verbose_name": "article plugin",
                "verbose_name_plural": "article plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="download",
            options={"verbose_name": "download", "verbose_name_plural": "downloads"},
        ),
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["start_date"],
                "verbose_name": "event",
                "verbose_name_plural": "events",
            },
        ),
        migrations.AlterModelOptions(
            name="eventplugin",
            options={
                "verbose_name": "event plugin",
                "verbose_name_plural": "event plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="image",
            options={"verbose_name": "image", "verbose_name_plural": "images"},
        ),
        migrations.AlterModelOptions(
            name="location",
            options={
                "ordering": ["name"],
                "verbose_name": "location",
                "verbose_name_plural": "locations",
            },
        ),
        migrations.AlterModelOptions(
            name="namespace",
            options={
                "ordering": ["name"],
                "verbose_name": "namespace",
                "verbose_name_plural": "namespaces",
            },
        ),
        migrations.AddField(
            model_name="event", name="uuid", field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="articles",
            field=models.ManyToManyField(
                blank=True,
                related_name="events_articleplugin",
                to="blog.Article",
                verbose_name="articles",
            ),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="sections.Category",
                verbose_name="category",
            ),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="count",
            field=models.IntegerField(default=3, verbose_name="count"),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="namespace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="blog.NameSpace",
                verbose_name="namespace",
            ),
        ),
        migrations.AlterField(
            model_name="articleplugin",
            name="title",
            field=models.CharField(blank=True, max_length=180, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="button",
            name="align",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "default"),
                    ("center", "center"),
                    ("right", "right"),
                    ("block", "block"),
                ],
                max_length=30,
                verbose_name="alignment",
            ),
        ),
        migrations.AlterField(
            model_name="button",
            name="style",
            field=models.CharField(
                blank=True,
                choices=[("", "none"), ("secondary", "secondary")],
                default="",
                max_length=20,
                verbose_name="style",
            ),
        ),
        migrations.AlterField(
            model_name="button",
            name="target",
            field=models.CharField(max_length=800, verbose_name="target"),
        ),
        migrations.AlterField(
            model_name="button",
            name="text",
            field=models.CharField(blank=True, max_length=240, verbose_name="text"),
        ),
        migrations.AlterField(
            model_name="download",
            name="document",
            field=models.FileField(upload_to="downloads/", verbose_name="File"),
        ),
        migrations.AlterField(
            model_name="download",
            name="download_text",
            field=models.CharField(max_length=200, verbose_name="download text"),
        ),
        migrations.AlterField(
            model_name="download",
            name="link_classes",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="link classes (css)"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="author",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sections.Category",
                verbose_name="category",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created at"),
        ),
        migrations.AlterField(
            model_name="event",
            name="edited_date",
            field=models.DateTimeField(auto_now=True, verbose_name="edited at"),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(verbose_name="end date"),
        ),
        migrations.AlterField(
            model_name="event",
            name="header_image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="header_image_height",
                null=True,
                upload_to="",
                verbose_name="header image",
                width_field="header_image_width",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="events.Location",
                verbose_name="location",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="namespace",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="events.NameSpace",
                verbose_name="namespace",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="publication_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="publication date"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sections.Section",
                verbose_name="section",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(verbose_name="start date"),
        ),
        migrations.AlterField(
            model_name="event",
            name="title",
            field=models.CharField(max_length=200, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                related_query_name="+",
                to="sections.Category",
                verbose_name="category",
            ),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="count",
            field=models.IntegerField(default=3, verbose_name="count"),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="events",
            field=models.ManyToManyField(
                blank=True,
                related_name="_eventplugin_events_+",
                related_query_name="+",
                to="events.Event",
                verbose_name="events",
            ),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="namespace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                related_query_name="+",
                to="events.NameSpace",
                verbose_name="namespace",
            ),
        ),
        migrations.AlterField(
            model_name="eventplugin",
            name="title",
            field=models.CharField(blank=True, max_length=180, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="formplugin",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events_formplugin",
                to="forms.Form",
                verbose_name="form",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="caption",
            field=models.CharField(blank=True, max_length=200, verbose_name="caption"),
        ),
        migrations.AlterField(
            model_name="image",
            name="title",
            field=models.CharField(blank=True, max_length=200, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="location",
            name="city",
            field=models.CharField(max_length=100, verbose_name="city"),
        ),
        migrations.AlterField(
            model_name="location",
            name="country",
            field=models.CharField(max_length=200, verbose_name="country"),
        ),
        migrations.AlterField(
            model_name="location",
            name="header_image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="header_image_height",
                null=True,
                upload_to="",
                verbose_name="header image",
                width_field="header_image_width",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.FloatField(default=0, verbose_name="latitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.FloatField(default=0, verbose_name="longitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(max_length=200, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="location",
            name="section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sections.Section",
                verbose_name="section",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="street",
            field=models.CharField(max_length=200, verbose_name="street"),
        ),
        migrations.AlterField(
            model_name="location",
            name="website",
            field=models.URLField(blank=True, verbose_name="website"),
        ),
        migrations.AlterField(
            model_name="location",
            name="zip_code",
            field=models.CharField(max_length=20, verbose_name="zip code"),
        ),
        migrations.AlterField(
            model_name="locationimage",
            name="caption",
            field=models.CharField(blank=True, max_length=200, verbose_name="caption"),
        ),
        migrations.AlterField(
            model_name="namespace",
            name="name",
            field=models.CharField(max_length=200, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="team",
            name="columns",
            field=models.CharField(
                choices=[("two", "2"), ("three", "3"), ("four", "4"), ("five", "5")],
                default="three",
                max_length=10,
                verbose_name="columns",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="people.Team",
                verbose_name="team",
            ),
        ),
    ]
