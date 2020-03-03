from fullapp.userprofile.models.games import Game
from fullapp.userprofile.models.cup import Cup
from django.db import models

class CupGames(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    cup_id = models.ForeignKey(Cup, on_delete=models.CASCADE)
    stage = models.IntegerField()
    prev_game_id = models.ForeignKey(Game,on_delete=models.SET_NULL)
