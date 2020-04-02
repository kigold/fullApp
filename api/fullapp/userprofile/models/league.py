from django.db import models


class League(models.Model):
    title = models.CharField(max_length=100, null=False)
    season = models.IntegerField()
