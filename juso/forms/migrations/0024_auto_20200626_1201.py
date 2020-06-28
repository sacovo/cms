# Generated by Django 3.0.5 on 2020-06-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0023_auto_20200624_2250"),
    ]

    operations = [
        migrations.AddField(
            model_name="form",
            name="meta_card_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("summary", "summary"),
                    ("summary large image", "summary_large_image"),
                    ("player", "player"),
                ],
                help_text="Card type",
                max_length=50,
                verbose_name="twitter card type",
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="meta_player",
            field=models.CharField(
                blank=True,
                help_text="HTTPS URL to iFrame player.",
                max_length=600,
                verbose_name="player url",
            ),
        ),
        migrations.AddField(
            model_name="form",
            name="meta_player_height",
            field=models.IntegerField(default=1080, verbose_name="player height"),
        ),
        migrations.AddField(
            model_name="form",
            name="meta_player_width",
            field=models.IntegerField(default=1920, verbose_name="player width"),
        ),
        migrations.AddField(
            model_name="form",
            name="meta_twitter_site",
            field=models.CharField(
                blank=True,
                help_text="The Twitter @username the card should be attributed to.",
                max_length=30,
                verbose_name="twitter site",
            ),
        ),
    ]
