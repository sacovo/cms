# Generated by Django 3.0.3 on 2020-03-31 19:22

import django.db.models.deletion
import django.utils.timezone
import imagefield.fields
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0004_auto_20200329_1551'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, help_text='Used for Open Graph and other meta tags.', max_length=200, verbose_name='title')),
                ('meta_description', models.TextField(blank=True, help_text='Override the description for this page.', verbose_name='description')),
                ('meta_image', imagefield.fields.ImageField(blank=True, height_field='meta_image_height', help_text='Set the Open Graph image.', upload_to='meta/%Y/%m', verbose_name='image', width_field='meta_image_width')),
                ('meta_canonical', models.URLField(blank=True, help_text='If you need this you probably know.', verbose_name='canonical URL')),
                ('meta_author', models.CharField(blank=True, help_text='Override the author meta tag.', max_length=200, verbose_name='author')),
                ('meta_robots', models.CharField(blank=True, help_text='Override the robots meta tag.', max_length=200, verbose_name='robots')),
                ('meta_image_width', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('meta_image_height', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('meta_image_ppoi', imagefield.fields.PPOIField(default='0.5x0.5', max_length=20)),
                ('template_key', models.CharField(choices=[('default', 'Default')], default='default', max_length=100, verbose_name='template')),
                ('language_code', models.CharField(choices=[('de', 'German'), ('fr', 'French'), ('it', 'Italian')], default='de', max_length=10, verbose_name='language')),
                ('title', models.CharField(max_length=200, verbose_name='Titel')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publication date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('edited_date', models.DateTimeField(auto_now=True, verbose_name='edited at')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sections.Category', verbose_name='category')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.Section', verbose_name='section')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('translations', models.ManyToManyField(blank=True, related_name='_form_translations_+', to='forms.Form')),
            ],
            options={
                'verbose_name': 'form',
                'verbose_name_plural': 'forms',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip address')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=140, verbose_name='name')),
                ('input_type', models.CharField(choices=[('', '')], max_length=140, verbose_name='type')),
                ('slug', models.SlugField()),
                ('required', models.BooleanField(verbose_name='required')),
                ('help_text', models.CharField(max_length=240, verbose_name='help_text')),
                ('choices', models.TextField(blank=True, verbose_name='choices')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms_formfield_set', to='forms.Form')),
            ],
            options={
                'ordering': ['ordering'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormEntryValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, verbose_name='value')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.FormField')),
                ('form_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.FormEntry')),
            ],
        ),
    ]
