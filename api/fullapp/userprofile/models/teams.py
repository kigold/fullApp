from django.db import models


class Team(models.Model):   
    Name = models.CharField(max_length=50, null=False)
    Country = models.CharField(max_length=50, null=False)

    class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_team'
