from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Game, Team, Profile
from ..serializers import GameSerializer, ProfileSerializer
from .setup import set_test_data
import datetime


class GameTest(APITestCase):
    def setUp(self):
        set_test_data()

    def test_create_game_fixtures(self):
        url = reverse('game-addfixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Game.objects.count(), 3,
                         "The Number of created games")

    def test_create_game_played_won(self):
        url = reverse('game-addfixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 3,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(Game.objects.count(), 3,
                         "The Number of created games")
        self.assertEqual(Game.objects.latest("pk").status, 2,
                         "Confirm game status")
        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Winner point decrease by 3")

    def test_create_game_played_drawn(self):
        url = reverse('game-addfixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Game.objects.count(), 3,
                         "The Number of created games")
        self.assertEqual(Game.objects.latest("pk").status, 2,
                         "Confirm game status")
        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23,
                         "users points doesnt change after draw")
        self.assertEqual(u1.points, 100,
                         "users points doesnt change after draw")

    def test_edit_game_played_draw(self):
        url = reverse('game-addfixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2,
                'status': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # url = reverse('game-updatefixtures', args=[2])
        url = "/games/fixtures/3"
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23,
                         "users points doesnt change after draw")
        self.assertEqual(u1.points, 100,
                         "users points doesnt change after draw")

    def test_edit_game_played_won(self):
        url = reverse('game-addfixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2,
                'status': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 3,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        # url = reverse('game-updatefixtures', args=[3])
        url = "/games/fixtures/3"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Losser point decrease by 3")

    def test_edit_already_played_game(self):
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 3,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        # url = reverse('game-updatefixtures', args=[2])
        url = "/games/fixtures/2"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data['error'], "Game already played, cannot update",
                         "Try updating already played game")

    def test_edit_game_postponed(self):
        url = reverse('game-updatefixtures', args=[2])
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 3}
        response = self.client.put(url, data, format='json')

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23,
                         "users points doesnt change after postpone")
        self.assertEqual(u1.points, 100,
                         "users points doesnt change after postpone")

    def test_edit_game_fixtures(self):
        url = reverse('game-updatefixtures', args=[2])
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 1}
        response = self.client.put(url, data, format='json')

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23,
                         "users points doesnt change after postpone")
        self.assertEqual(u1.points, 100,
                         "users points doesnt change after postpone")

    def test_get_game(self):
        # url = reverse('game-fixtures')
        url = "/games/fixtures/"
        response = self.client.get(url)
        data = response.data['results']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[1]['home_score'], 4)
        self.assertEqual(data[1]['away_score'], 3)
        self.assertEqual(data[1]['home_user']['nick_name'],
                         "admino")
        self.assertEqual(data[1]['home_user']['user']
                         ['email'], "admin@yahoo.com")
        self.assertEqual(data[0]['home_user']['nick_name'],
                         "ninetail")
        self.assertEqual(data[0]['home_user']['user']
                         ['email'], "naruto@konoha.com")
        self.assertEqual(data[0]['home_user']['user']
                         ['first_name'], "naruto")
