from .game import Game
from .cup import Cup
from django.db import models


class CupGame(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="game")
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE)
    stage = models.IntegerField()
    prev_game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="prev_game")

    '''class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_cupgame'

'''
