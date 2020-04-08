from django.db import models
from . import Team, Profile
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):

    class Game_Status(models.IntegerChoices):
        Fixtured = 1
        Played = 2
        Postponed = 3
    '''GAME_STATUS = [
        (1, "Fixture"),
        (2, "Played"),
        (3, "Postponed")
    ]'''
    away_user = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                  related_name="away_team_user",
                                  to_field='user_id',
                                  default=1)
    away_score = models.IntegerField()
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name="away_team",
                                  to_field='id',
                                  default=1)
    home_user = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                  related_name="home_team_user",
                                  to_field='user_id',
                                  default=1)
    home_score = models.IntegerField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name="home_team",
                                  to_field='id',
                                  default=1)
    penalty_shootout = models.BooleanField()
    date_played = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(
        choices=Game_Status.choices,
        default=Game_Status.choices[0])
    '''status = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)],
        choices=GAME_STATUS,
        default=1
    )'''
