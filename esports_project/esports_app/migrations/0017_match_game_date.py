# Generated by Django 4.1.3 on 2022-12-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0016_remove_match_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='game_date',
            field=models.DateField(null=True),
        ),
    ]