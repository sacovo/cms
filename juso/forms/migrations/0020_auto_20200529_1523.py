# Generated by Django 3.0.5 on 2020-05-29 13:23

from django.db import migrations, models
import imagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0019_auto_20200523_1748"),
    ]

    operations = [
        migrations.AddField(
            model_name="form",
            name="generated_meta_image",
            field=imagefield.fields.ImageField(
                blank=True,
                height_field="generated_meta_image_height",
                null=True,
                upload_to="",
                verbose_name="generated meta image",
                width_field="generated_meta_image_width",
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="generated_meta_image_height",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="form",
            name="generated_meta_image_ppoi",
            field=imagefield.fields.PPOIField(default="0.5x0.5", max_length=20),
        ),
        migrations.AddField(
            model_name="form",
            name="generated_meta_image_width",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
