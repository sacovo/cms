# Generated by Django 3.0.3 on 2020-02-15 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_auto_20200215_2215"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="application",
            field=models.CharField(
                blank=True,
                choices=[("blog", "blog"), ("people", "people"), ("events", "events")],
                max_length=20,
                verbose_name="application",
            ),
        ),
        migrations.CreateModel(
            name="Download",
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
                    "document",
                    models.FileField(upload_to="downloads/", verbose_name="Datei"),
                ),
                (
                    "download_text",
                    models.CharField(max_length=200, verbose_name="download text"),
                ),
                (
                    "link_classes",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="link classes (css)"
                    ),
                ),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pages_download_set",
                        to="pages.Page",
                    ),
                ),
            ],
            options={
                "verbose_name": "download",
                "verbose_name_plural": "downloads",
                "abstract": False,
            },
        ),
    ]
