# Generated by Django 3.0.5 on 2020-05-10 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0033_auto_20200510_1834"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eventplugin", old_name="all_articles", new_name="all_events",
        ),
        migrations.RenameField(
            model_name="eventplugin",
            old_name="all_articles_override",
            new_name="all_events_override",
        ),
    ]
