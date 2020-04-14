from django.db import models
from . import Game, League


class LeagueGame(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="league_game")
    league = models.ForeignKey(
        League, on_delete=models.CASCADE, related_name="league")

    class Meta:
        ordering = ['-pk']
