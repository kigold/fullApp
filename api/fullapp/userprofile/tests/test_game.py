from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Game, Team, Profile
from ..serializers import GameSerializer, ProfileSerializer
import datetime


class GameTest(APITestCase):
    def setUp(self):
        Team.objects.create(name="Eyimba", country="Nigeria")
        Team.objects.create(name="PSG", country="France")
        p1 = ProfileSerializer(
            data={'nick_name': 'admino', 'points': 100, 'fav_team_id': 1,
                  'user': {'username': 'admin', 'email': 'admin@yahoo.com',
                           'is_staff': True, 'first_name': 'admin',
                           'last_name': 'badoo',
                           'is_active': True, 'password': 'P@ssw0rd'}})
        p2 = ProfileSerializer(
            data={'nick_name': 'ninetail', 'points': 23, 'fav_team_id': 1,
                  'user': {'username': 'naruto', 'email': 'naruto@konoha.com',
                           'is_staff': False, 'first_name': 'naruto',
                           'last_name': 'uzumaki',
                           'is_active': True, 'password': 'P@ssw0rd'}})
        p1.is_valid()
        p1.save()
        p2.is_valid()
        p2.save()
        g1 = GameSerializer(
            data={'home_user_id': 1, 'away_user_id': 2,
                  'home_team_id': 1, 'away_team_id': 1, 'home_score': 4,
                  'away_score': 3, 'penalty_shootout': False,
                  'date_played': datetime.datetime.now(),
                  'status': 2})
        g1.is_valid()
        g1.save()
        g2 = GameSerializer(
                data={'home_user_id': 2, 'away_user_id': 1,
                      'home_team_id': 2, 'away_team_id': 2, 'home_score': 2,
                      'away_score': 1, 'penalty_shootout': False,
                      'date_played': datetime.datetime.now(),
                      'status': 2})
        g2.is_valid()
        g2.save()
        print(Game.objects.all())

    def test_create_game_fixtures(self):
        url = reverse('game-fixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 3,
                         "The Number of created games")

    def test_create_game_played_won(self):
        url = reverse('played')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 3,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 3,
                         "The Number of created games")
        self.assertEqual(Profile.objects.latest("pk").status, 2,
                         "Confirm game status")
        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Winner point decrease by 3")

    def test_create_game_played_drawn(self):
        url = reverse('game-fixtures')
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 3,
                         "The Number of created games")
        self.assertEqual(Profile.objects.latest("pk").status, 2,
                         "Confirm game status")
        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23,
                         "users points doesnt change after draw")
        self.assertEqual(u1.points, 100,
                         "users points doesnt change after draw")

    def test_edit_game_played_draw(self):
        url = reverse('game-fixtures', args=[2])
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 1,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.put(url, data, format='json')

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 23,
                         "users points doesnt change after draw")
        self.assertEqual(u1.points, 100,
                         "users points doesnt change after draw")

    def test_edit_game_played_won(self):
        url = reverse('fixture', args=[2])
        data = {'home_user_id': 2, 'away_user_id': 1,
                'home_team_id': 2, 'away_team_id': 2, 'home_score': 3,
                'away_score': 1, 'penalty_shootout': False,
                'date_played': datetime.datetime.now(),
                'status': 2}
        response = self.client.put(url, data, format='json')

        u2 = Profile.objects.get(pk=2)
        u1 = Profile.objects.get(pk=1)
        self.assertEqual(u2.points, 26, "Winner point increase by 3")
        self.assertEqual(u1.points, 97, "Winner point decrease by 3")

    def test_edit_game_postponed(self):
        url = reverse('fixture', args=[2])
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
        url = reverse('fixture', args=[2])
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
        url = reverse('games')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['home_score'], 4)
        self.assertEqual(response.data['results'][0]['away_score'], 3)
        self.assertEqual(response.data['results'][0]['home_user']['nick_name'],
                         "admino")
        self.assertEqual(response.data['results'][0]['home_user']['user']
                         ['email'], "admin@yahoo.com")
        self.assertEqual(response.data['results'][1]['home_user']['nick_name'],
                         "ninetail")
        self.assertEqual(response.data['results'][1]['home_user']['user']
                         ['email'], "naruto@konoha.com")
        self.assertEqual(response.data['results'][1]['home_user']['user']
                         ['first_name'], "naruto")
