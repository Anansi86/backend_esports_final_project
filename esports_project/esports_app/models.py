from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #custom_field = models.CharField(blank=True, max_length=60)
    custom_field = 0

class Team(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)
    icon = models.URLField(max_length=200)
    users = models.ManyToManyField(CustomUser, related_name="teams")

    def __str__(self):
        return self.name

class Match(models.Model):
    win = models.CharField(max_length=25, blank=False, null=False)
    video_url = models.TextField()
    game_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    team1 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="Team1")
    team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="Team2")
    status = models.IntegerField()
    users = models.ManyToManyField(CustomUser, related_name="matches")
    

def __str__(self):
        return str(self.created)

class Player(models.Model):
    player_name = models.CharField(max_length=25, blank=False, unique=True)
    alias_name = models.CharField(max_length=25, blank=False, unique=True)
    player_num = models.IntegerField()
    hometown = models.CharField(max_length=25, blank=False, unique=False)
    pic = models.URLField()
    team = models.ManyToManyField(Team, related_name='players')
    total_damage = models.IntegerField(null=True)
    total_eliminations = models.IntegerField(null=True)
    total_deaths = models.IntegerField(null=True)

    def __str__(self):
        return self.player_name

class Hero(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)
    character_img = models.URLField()
    main_attack = models.CharField(max_length=25, blank=False, unique=True)
    special_attack = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.name

class Hero_player_matches(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    hero_id = models.ForeignKey(Hero, on_delete=models.SET_NULL, null=True)
    match_id = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()

    def __str__(self):
        return str(self.points)

class Match_score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True, related_name="scores")
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()

    def __str__(self):
        if self.match is None:
            return "No Match"
        else:
            return str(self.match.id)
