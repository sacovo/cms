# Generated by Django 3.0.3 on 2020-02-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0004_auto_20200215_2128"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="membership",
            options={
                "ordering": ["order"],
                "verbose_name": "membership",
                "verbose_name_plural": "memberships",
            },
        ),
        migrations.AlterModelOptions(
            name="team",
            options={
                "ordering": ["order"],
                "verbose_name": "team",
                "verbose_name_plural": "teams",
            },
        ),
        migrations.AddField(
            model_name="membership",
            name="order",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="team",
            name="order",
            field=models.IntegerField(default=1, verbose_name="order"),
            preserve_default=False,
        ),
    ]
