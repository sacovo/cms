# Generated by Django 3.0.3 on 2020-03-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sections", "0003_auto_20200302_1952"),
        ("pages", "0022_merge_20200328_1757"),
    ]

    operations = [
        migrations.RemoveField(model_name="page", name="all_events",),
        migrations.AddField(
            model_name="page",
            name="featured_categories",
            field=models.ManyToManyField(
                blank=True,
                related_name="_page_featured_categories_+",
                related_query_name="+",
                to="sections.Category",
                verbose_name="featured categories",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="sections",
            field=models.ManyToManyField(
                blank=True,
                related_name="_page_sections_+",
                related_query_name="+",
                to="sections.Section",
                verbose_name="sections",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="application",
            field=models.CharField(
                blank=True,
                choices=[
                    ("blog", "blog"),
                    ("people", "people"),
                    ("events", "events"),
                    ("categories", "categories"),
                ],
                max_length=20,
                verbose_name="application",
            ),
        ),
    ]
