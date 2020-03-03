from django.db import models


class Challenge(models.Model):    
    away_user_id = models.IntegerField() 
    away_score = models.IntegerField()   
    away_team_id = models.IntegerField()    
    home_user_id = models.IntegerField()
    home_score = models.IntegerField()
    home_team_id = models.IntegerField()
    penalty_shootout = models.BooleanField() 
    date_played = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_challenge'