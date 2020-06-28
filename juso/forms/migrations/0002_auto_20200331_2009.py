# Generated by Django 3.0.3 on 2020-03-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="formfield",
            name="initial",
            field=models.TextField(blank=True, max_length=240, verbose_name="initial"),
        ),
        migrations.AlterField(
            model_name="formfield",
            name="input_type",
            field=models.CharField(
                choices=[
                    ("text", "text"),
                    ("email", "email"),
                    ("boolean", "boolean"),
                    ("date", "date"),
                    ("datetime", "datetime"),
                    ("time", "time"),
                    ("decimal", "decimal"),
                    ("file", "file"),
                    ("image", "image"),
                    ("int", "integer"),
                    ("choice", "choice"),
                    ("multi", "multiple choice"),
                    ("url", "url"),
                    ("hidden", "hidden"),
                ],
                max_length=140,
                verbose_name="type",
            ),
        ),
    ]
