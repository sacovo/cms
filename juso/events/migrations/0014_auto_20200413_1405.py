# Generated by Django 3.0.3 on 2020-04-13 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0013_divider_header"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["start_date"],
                "verbose_name": "event",
                "verbose_name_plural": "events",
            },
        ),
    ]
