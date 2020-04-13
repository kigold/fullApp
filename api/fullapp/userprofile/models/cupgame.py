from django.db import models
from . import Game, Cup


class CupGame(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="cup_game")
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE)
    stage = models.IntegerField()
    prev_game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="prev_game",
        null=True, blank=True)

    '''class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_cupgame'

'''
