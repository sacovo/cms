# Generated by Django 3.0.3 on 2020-03-28 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_merge_20200324_2216'),
        ('sections', '0003_auto_20200302_1952'),
        ('blog', '0009_merge_20200324_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(choices=[('de', 'German'), ('fr', 'French'), ('it', 'Italian')], default='de', max_length=10, verbose_name='language')),
                ('count', models.IntegerField(default=3, verbose_name='count')),
                ('template_key', models.CharField(choices=[('events/plugins/default.html', 'default')], default='events/default.html', max_length=100)),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='+', to='sections.Category', verbose_name='category')),
                ('events', models.ManyToManyField(blank=True, related_name='_eventplugin_events_+', related_query_name='+', to='events.Event', verbose_name='events')),
                ('namespace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='+', to='events.NameSpace', verbose_name='namespace')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_eventplugin_set', to='blog.Article')),
                ('sections', models.ManyToManyField(blank=True, related_name='_eventplugin_sections_+', related_query_name='+', to='sections.Section')),
                ('translations', models.ManyToManyField(blank=True, related_name='_eventplugin_translations_+', to='blog.EventPlugin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
