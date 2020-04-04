from django.db import models
from . import Team, Profile


class Game(models.Model):
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
