# Generated by Django 3.0.5 on 2020-05-08 14:10

from django.db import migrations, models
import django.db.models.deletion
import feincms3.cleanse


class Migration(migrations.Migration):

    dependencies = [
        ("sections", "0009_auto_20200507_1758"),
        ("pages", "0038_auto_20200507_1758"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="articleplugin",
            options={
                "verbose_name": "Artikel plugin",
                "verbose_name_plural": "Artikel plugin",
            },
        ),
        migrations.AlterModelOptions(
            name="eventplugin",
            options={
                "verbose_name": "event plugin",
                "verbose_name_plural": "Event plugins",
            },
        ),
        migrations.CreateModel(
            name="CategoryLinking",
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
                ("description", feincms3.cleanse.CleansedRichTextField()),
                ("order", models.IntegerField(default=10)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sections.Category",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.Page"
                    ),
                ),
            ],
            options={"ordering": ["order"],},
        ),
    ]
