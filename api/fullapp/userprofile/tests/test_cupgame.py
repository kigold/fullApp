from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Game, Team, Profile, Cup
import datetime
from ..serializers import GameSerializer, ProfileSerializer, CupSerializer,\
    CupGameSerializer
from .setup import *


class CupGameTest(APITestCase):
    def setUp(self):
        set_test_data()
        set_cup_data()

    def test_create_cup(self):
        url = reverse('cup-list')
        data = {'name': 'Another Cup'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cup.objects.count(), 2,
                         "The Number of created cups")
        self.assertEqual(Cup.objects.get(pk=2).name, 'Another Cup',
                         "The name of the Cup")

    def test_create_cup_game(self):
        url = reverse('cupgame-list')
        data = {'cup_id': 1, 'stage': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 1, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 5,
                         "The Number of created cup games")

    def test_edit_cup_Fixture(self):
        url = reverse('cupgame-list')
        data = {'cup_id': 1, 'stage': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1,
                         'status': 1}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 5,
                         "The Number of created cup games")
        data = {'cup_id': 1, 'stage': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 7, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        url = reverse('cupgame-detail', args=[3])
        print(url)
        # url = "/games/fixtures/2"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CupGame.objects.count(), 3,
                         "The Number of created cup games")

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Losser point decrease by 3")

    def test_edit_cup_Fixture_failed(self):
        data = {'cup_id': 1, 'stage': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 7, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        url = reverse('cupgame-detail', args=[2])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response, "Game already played cannot update",
                            status_code=status.HTTP_400_BAD_REQUEST)

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23, "user points unchanged")
        self.assertEqual(u1.points, 100, "user points unchanged")
