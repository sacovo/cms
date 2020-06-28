# Generated by Django 3.0.5 on 2020-05-10 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sections", "0009_auto_20200507_1758"),
        ("forms", "0018_auto_20200509_1826"),
        ("pages", "0044_auto_20200510_1139"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventplugin",
            name="sections",
            field=models.ManyToManyField(
                blank=True, related_name="pages_eventplugin", to="sections.Section"
            ),
        ),
        migrations.AlterField(
            model_name="formplugin",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages_formplugin",
                to="forms.Form",
                verbose_name="Formular",
            ),
        ),
    ]
