from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from .team import Team


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    # REQUIRED_FIELDS = []

    def __str__(self):
        return "{}".format(self.email)


class Profile(models.Model):
    '''def __init__(self, user_id, email, nick_name, is_staff=False):
        self.user_id = user_id
        self.email = email
        self.nick_name = nick_name
        self.is_staff = is_staff
        self.is_active = True'''

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    '''goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    game_drawn = models.IntegerField()
    game_lose = models.IntegerField()
    game_won = models.IntegerField()'''
    nick_name = models.CharField(max_length=50, null=False)
    points = models.IntegerField()

    class Meta:
        ordering = ['pk']

    '''class Meta:
        app_label = 'userprofile'
        db_table = 'fullapp_profile'
        '''
