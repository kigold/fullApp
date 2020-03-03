from fullapp.userprofile.models.games import Game
from django.db import models


class League(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    version = models.IntegerField()