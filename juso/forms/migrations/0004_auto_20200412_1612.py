# Generated by Django 3.0.3 on 2020-04-12 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200402_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formentry',
            options={'verbose_name': 'form entry', 'verbose_name_plural': 'form entries'},
        ),
        migrations.AlterModelOptions(
            name='formentryvalue',
            options={'verbose_name': 'form entry value', 'verbose_name_plural': 'form entry values'},
        ),
        migrations.AlterModelOptions(
            name='formfield',
            options={'ordering': ['ordering'], 'verbose_name': 'form field', 'verbose_name_plural': 'form fields'},
        ),
    ]