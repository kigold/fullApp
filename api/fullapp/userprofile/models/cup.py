from django.db import models

class Cup(models.Model):
    Name = models.CharField(max_length=100, null=False)