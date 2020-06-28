# Generated by Django 3.0.5 on 2020-06-24 20:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0058_auto_20200624_2235"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="meta_video_url",
            field=models.URLField(
                blank=True,
                help_text="Set the Open Graph video to an url.",
                verbose_name="video url",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="meta_video",
            field=models.FileField(
                blank=True,
                help_text="Set the Open Graph video.",
                upload_to="meta/video/%Y/%m",
                validators=[django.core.validators.FileExtensionValidator(["mp4"])],
                verbose_name="video",
            ),
        ),
    ]
