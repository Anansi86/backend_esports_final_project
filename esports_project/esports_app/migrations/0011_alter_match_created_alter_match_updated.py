# Generated by Django 4.1.3 on 2022-12-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0010_rename_match_id_match_score_match_remove_match_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
