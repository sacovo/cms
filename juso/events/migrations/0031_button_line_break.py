# Generated by Django 3.0.5 on 2020-05-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0030_auto_20200510_1723"),
    ]

    operations = [
        migrations.AddField(
            model_name="button",
            name="line_break",
            field=models.BooleanField(default=True, verbose_name="break"),
        ),
    ]
