from django.db import models


class Cup(models.Model):
    name = models.CharField(max_length=100, null=False)

    '''class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_cup'
'''
