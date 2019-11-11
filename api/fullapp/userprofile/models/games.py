from django.db import models


class Game(models.Model):    
    away_user_id = models.IntegerField() 
    away_score = models.IntegerField()   
    away_team_id = models.IntegerField()    
    home_user_id = models.IntegerField()
    home_score = models.IntegerField()
    home_team_id = models.IntegerField()
    penalty_shootout = models.BooleanField()  
    '''
    class Meta:
        app_name = 'fullapp'
        db_table = 'fullapp_game'
    '''