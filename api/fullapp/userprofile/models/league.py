from django.db import models

class League(models.Model):
    game_id = models.ForeignKey(Game)