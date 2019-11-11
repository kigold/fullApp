from django.db import models


class Profile(models.Model):
    fav_team_id = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()    
    game_drawn = models.IntegerField()
    game_lose = models.IntegerField()    
    game_won = models.IntegerField()
    nick_name = models.CharField(max_length=50, null=False)
    points = models.IntegerField()
    '''
    class Meta:
        app_name = 'fullapp'
        db_table = 'fullapp_profile'
    '''