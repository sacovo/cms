# Generated by Django 3.0.3 on 2020-03-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0006_auto_20200302_1544"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="language_code",
            field=models.CharField(
                choices=[("de", "German"), ("fr", "French"), ("it", "Italian")],
                default="de",
                max_length=10,
                verbose_name="language",
            ),
        ),
        migrations.AddField(
            model_name="location",
            name="translations",
            field=models.ManyToManyField(
                related_name="_location_translations_+", to="events.Location"
            ),
        ),
        migrations.AddField(
            model_name="namespace",
            name="translations",
            field=models.ManyToManyField(
                related_name="_namespace_translations_+", to="events.NameSpace"
            ),
        ),
    ]
