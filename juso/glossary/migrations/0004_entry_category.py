# Generated by Django 3.0.3 on 2020-04-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sections", "0004_auto_20200329_1551"),
        ("glossary", "0003_auto_20200416_2112"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sections.Category",
            ),
        ),
    ]
