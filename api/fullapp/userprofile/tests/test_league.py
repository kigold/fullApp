from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Game, Team, Profile, LeagueGame
import datetime
from ..serializers import GameSerializer, ProfileSerializer, LeagueSerializer,\
    LeagueGameSerializer
from .setup import *


class LeagueGameTest(APITestCase):
    def setUp(self):
        set_test_data()
        set_league_data()

    def test_create_league(self):
        url = reverse('league-list')
        data = {'title': 'Another League', 'season': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(League.objects.count(), 2,
                         "The Number of created leagues")
        self.assertEqual(League.objects.get(pk=2).title, 'Another League',
                         "The name of the League")

    def test_create_league_game(self):
        url = reverse('leaguegame-list')
        data = {'league_id': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 1, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 5,
                         "The Number of created league games")
    
    def test_create_league_game_for_invalid_league_fail(self):
        url = reverse('leaguegame-list')
        data = {'league_id': 20,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 1, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        response = self.client.post(url, data, format='json')   
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response, "No League matches the given query",
                            status_code=status.HTTP_400_BAD_REQUEST)

    def test_edit_league_Fixture(self):
        url = reverse('leaguegame-list')
        data = {'league_id': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1,
                         'status': 1}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 5,
                         "The Number of created league games")
        data = {'league_id': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 7, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        url = reverse('leaguegame-detail', args=[3])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(LeagueGame.objects.count(), 3,
                         "The Number of created league games")

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Losser point decrease by 3")

    def test_edit_league_Fixture_failed(self):
        data = {'league_id': 1,
                'game': {'home_user_id': 1, 'away_user_id': 2,
                         'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                         'away_score': 7, 'penalty_shootout': False,
                         'date_played': datetime.datetime.now(),
                         'status': 2}}
        url = reverse('leaguegame-detail', args=[2])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response, "Game already played cannot update",
                            status_code=status.HTTP_400_BAD_REQUEST)

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23, "user points unchanged")
        self.assertEqual(u1.points, 100, "user points unchanged")
