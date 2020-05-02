# Generated by Django 3.0.3 on 2020-04-16 22:03

from django.db import migrations, models
import django.db.models.deletion
import feincms3.cleanse


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0003_auto_20200416_2112'),
        ('blog', '0012_merge_20200328_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlossaryRichText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', feincms3.cleanse.CleansedRichTextField(verbose_name='text')),
                ('glossary_text', models.TextField(blank=True)),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('entries', models.ManyToManyField(related_name='blog_glossaryrichtext_related', related_query_name='blog_glossaryrichtexts', to='glossary.Entry', verbose_name='entries')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_glossaryrichtext_set', to='blog.Article')),
            ],
            options={
                'verbose_name': 'glossary text',
            },
        ),
    ]