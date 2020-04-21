from django.db import models
from .game import Game, Profile


class Challenge(models.Model):
    challenged = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                   related_name="challenged_user",
                                   to_field='user_id',
                                   default=1)
    challenger = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                   related_name="challenger_user",
                                   to_field='user_id',
                                   default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True,
                             related_name="challenge_game")
    proposed_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-pk']
