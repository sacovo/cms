# Generated by Django 3.0.3 on 2020-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_auto_20200215_1901"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["-start_date"],
                "verbose_name": "event",
                "verbose_name_plural": "events",
            },
        ),
        migrations.AlterModelOptions(
            name="location",
            options={"verbose_name": "location", "verbose_name_plural": "locations"},
        ),
        migrations.AlterField(
            model_name="location",
            name="city",
            field=models.CharField(max_length=100, verbose_name="city"),
        ),
        migrations.AlterField(
            model_name="location",
            name="country",
            field=models.CharField(max_length=200, verbose_name="country"),
        ),
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.FloatField(verbose_name="latitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.FloatField(verbose_name="longitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="location",
            name="street",
            field=models.CharField(max_length=200, verbose_name="street"),
        ),
        migrations.AlterField(
            model_name="location",
            name="website",
            field=models.URLField(blank=True, verbose_name="website"),
        ),
        migrations.AlterField(
            model_name="location",
            name="zip_code",
            field=models.CharField(max_length=20, verbose_name="zip code"),
        ),
        migrations.AlterField(
            model_name="namespace",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Name"),
        ),
        migrations.AlterUniqueTogether(name="event", unique_together=set(),),
    ]
