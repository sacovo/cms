# Generated by Django 3.0.3 on 2020-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20200215_1901"),
    ]

    operations = [
        migrations.AlterField(
            model_name="namespace",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Name"),
        ),
    ]
