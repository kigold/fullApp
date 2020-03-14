from .game import Game
from django.db import models


class Challenge(models.Model):
    challenged_id = models.IntegerField()
    challenger_id = models.IntegerField()
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    proposed_date = models.DateTimeField(null=True, blank=True)
