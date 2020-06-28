# Generated by Django 3.0.3 on 2020-03-24 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0011_team_columns"),
    ]

    operations = [
        migrations.CreateModel(
            name="Button",
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
                ("text", models.CharField(max_length=240, verbose_name="Text")),
                (
                    "inverted",
                    models.BooleanField(default=False, verbose_name="inverted"),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, choices=[("red", "red")], max_length=20
                    ),
                ),
                (
                    "style",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "none"),
                            ("basic", "basic"),
                            ("primary", "primary"),
                            ("tertiary", "tertiary"),
                        ],
                        default="",
                        max_length=20,
                        verbose_name="style",
                    ),
                ),
                ("target", models.CharField(max_length=800, verbose_name="Ziel")),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pages_button_set",
                        to="pages.Page",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
