# Generated by Django 4.1.3 on 2022-12-04 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0009_match_users_team_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match_score',
            old_name='match_id',
            new_name='match',
        ),
        migrations.RemoveField(
            model_name='match',
            name='score',
        ),
    ]
