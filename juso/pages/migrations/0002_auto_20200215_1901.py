# Generated by Django 3.0.3 on 2020-02-15 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pages", "0001_initial"),
        ("blog", "0001_initial"),
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="people.Team",
                verbose_name="team",
            ),
        ),
        migrations.AddField(
            model_name="richtext",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages_richtext_set",
                to="pages.Page",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="blog_namespace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blog.NameSpace",
                verbose_name="namespace",
            ),
        ),
    ]
