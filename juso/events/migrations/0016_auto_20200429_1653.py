# Generated by Django 3.0.3 on 2020-04-29 16:53

from django.db import migrations, models
import django.db.models.deletion
import juso.models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0012_auto_20200426_1301"),
        ("blog", "0015_auto_20200429_1653"),
        ("sections", "0005_category_color"),
        ("events", "0015_merge_20200414_1907"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticlePlugin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        choices=[("de", "German"), ("fr", "French"), ("it", "Italian")],
                        default="de",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                ("count", models.IntegerField(default=3, verbose_name="count")),
                (
                    "template_key",
                    models.CharField(
                        choices=[("blog/plugins/default.html", "default")],
                        default="blog/plugins/default.html",
                        max_length=100,
                    ),
                ),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "articles",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_articleplugin_articles_+",
                        related_query_name="+",
                        to="blog.Article",
                        verbose_name="articles",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="sections.Category",
                        verbose_name="category",
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="blog.NameSpace",
                        verbose_name="namespace",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events_articleplugin_set",
                        to="events.Event",
                    ),
                ),
                (
                    "sections",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_articleplugin_sections_+",
                        related_query_name="+",
                        to="sections.Section",
                    ),
                ),
                (
                    "translations",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_articleplugin_translations_+",
                        to="events.ArticlePlugin",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="EventPlugin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        choices=[("de", "German"), ("fr", "French"), ("it", "Italian")],
                        default="de",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                ("count", models.IntegerField(default=3, verbose_name="count")),
                (
                    "template_key",
                    models.CharField(
                        choices=[("events/plugins/default.html", "default")],
                        default="events/plugins/default.html",
                        max_length=100,
                    ),
                ),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        related_query_name="+",
                        to="sections.Category",
                        verbose_name="category",
                    ),
                ),
                (
                    "events",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_eventplugin_events_+",
                        related_query_name="+",
                        to="events.Event",
                        verbose_name="events",
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        related_query_name="+",
                        to="events.NameSpace",
                        verbose_name="namespace",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events_eventplugin_set",
                        to="events.Event",
                    ),
                ),
                (
                    "sections",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_eventplugin_sections_+",
                        related_query_name="+",
                        to="sections.Section",
                    ),
                ),
                (
                    "translations",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_eventplugin_translations_+",
                        to="events.EventPlugin",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="FormPlugin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        related_query_name="+",
                        to="forms.Form",
                        verbose_name="form",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events_formplugin_set",
                        to="events.Event",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.RemoveField(model_name="header", name="parent",),
        migrations.RemoveField(model_name="button", name="inverted",),
        migrations.AlterField(
            model_name="button",
            name="color",
            field=juso.models.ColorField(
                blank=True,
                choices=[
                    ("red", "red"),
                    ("orange", "orange"),
                    ("yellow", "yellow"),
                    ("olive", "olive"),
                    ("green", "green"),
                    ("teal", "teal"),
                    ("violett", "violett"),
                    ("purple", "purple"),
                    ("pink", "pink"),
                    ("brown", "brown"),
                    ("grey", "grey"),
                    ("black", "black"),
                ],
                max_length=20,
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
        migrations.DeleteModel(name="Divider",),
        migrations.DeleteModel(name="Header",),
    ]
