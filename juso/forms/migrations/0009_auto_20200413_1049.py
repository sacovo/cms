# Generated by Django 3.0.3 on 2020-04-13 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20200413_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentryvalue',
            name='form_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='forms.FormEntry'),
        ),
    ]