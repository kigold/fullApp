from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_team_id = models.IntegerField()
    '''goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    game_drawn = models.IntegerField()
    game_lose = models.IntegerField()
    game_won = models.IntegerField()'''
    nick_name = models.CharField(max_length=50, null=False)
    points = models.IntegerField()

    '''class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_profile'
        '''
