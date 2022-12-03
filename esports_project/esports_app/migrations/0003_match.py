# Generated by Django 4.1.3 on 2022-12-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0002_remove_customuser_fav_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.CharField(max_length=25, unique=True)),
                ('video_url', models.TextField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]