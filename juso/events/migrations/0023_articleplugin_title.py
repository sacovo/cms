# Generated by Django 3.0.5 on 2020-05-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_image_fullwidth'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleplugin',
            name='title',
            field=models.CharField(blank=True, max_length=180, verbose_name='Titel'),
        ),
    ]
