# Generated by Django 3.0.5 on 2020-07-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0072_auto_20200720_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='prefetches',
            field=models.TextField(default='fonts/klima-bold-italic-web.woff2:font\nfonts/klima-ultra-web.woff2:font\nklima-regular-web.woff2:font', help_text='files that should be preloaded', verbose_name='prefetch'),
        ),
        migrations.AlterField(
            model_name='page',
            name='template_key',
            field=models.CharField(choices=[('default', 'Standard'), ('no_header_image', 'No_Header_Image'), ('sidebar-right', 'Sidebar-Right'), ('sidebar-left', 'Sidebar-Left'), ('sidebar-both', 'Sidebar-Both'), ('fullwidth', 'Fullwidth')], default='default', max_length=100, verbose_name='template'),
        ),
    ]