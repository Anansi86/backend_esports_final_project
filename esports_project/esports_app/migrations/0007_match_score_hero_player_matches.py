# Generated by Django 4.1.3 on 2022-12-03 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0006_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1_score', models.IntegerField()),
                ('team2_score', models.IntegerField()),
                ('match_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scores', to='esports_app.match')),
            ],
        ),
        migrations.CreateModel(
            name='Hero_player_matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('hero_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esports_app.hero')),
                ('match_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esports_app.match')),
                ('player_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esports_app.player')),
            ],
        ),
    ]
