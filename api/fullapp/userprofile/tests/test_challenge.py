from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Game, Team, Profile, LeagueGame, Challenge
import datetime
from ..serializers import GameSerializer, ProfileSerializer, LeagueSerializer,\
    LeagueGameSerializer, ChallengeSerializer
from .setup import *


class ChallengeTest(APITestCase):
    def setUp(self):
        set_test_data()
        set_challenge_data()

    def test_create_challenge(self):
        url = reverse('challenge-list')
        data = {'challenger_id': 1, 'challenged_id': 2,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1,
                         'status': 1}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 5,
                         "The Number of created games")
        self.assertEqual(Challenge.objects.count(), 3,
                         "The Number of challenge")

    def test_edit_Challenge_Fixture(self):
        url = reverse('challenge-list')
        data = {'challenger_id': 1, 'challenged_id': 2,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1,
                         'status': 1}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 5,
                         "The Number of created league games")
        self.assertEqual(Challenge.objects.count(), 3,
                         "The Number of challenge")

        data = {'challenged_id': 1, 'challenger_id': 2,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 7, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        url = reverse('challenge-detail', args=[3])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Challenge.objects.count(), 3,
                         "The Number of challenge")

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Losser point decrease by 3")
