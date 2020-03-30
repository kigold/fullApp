from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
