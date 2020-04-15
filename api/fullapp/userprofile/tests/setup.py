import datetime
from ..models import Game, Team, Profile, Cup, CupGame, League
from ..serializers import GameSerializer, ProfileSerializer,\
    CupGameSerializer, LeagueSerializer, LeagueGameSerializer


def set_test_data():
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


def set_cup_data():
    Cup.objects.create(name="Test Cup")
    g1 = CupGameSerializer(
        data={'cup_id': 1, 'stage': 1,
              'game': {'home_user_id': 1, 'away_user_id': 2,
                       'home_team_id': 1, 'away_team_id': 1, 'home_score': 5,
                       'away_score': 3, 'penalty_shootout': False,
                       'date_played': datetime.datetime.now(),
                       'status': 2}})
    g1.is_valid()
    g1.save()
    g2 = CupGameSerializer(
        data={'cup_id': 1, 'stage': 1,
              'game': {'home_user_id': 1, 'away_user_id': 2,
                       'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                       'away_score': 1, 'penalty_shootout': False,
                       'date_played': datetime.datetime.now(),
                       'status': 2}})
    g2.is_valid()
    g2.save()


def set_league_data():
    League.objects.create(title="Test League", season=1)
    g1 = LeagueGameSerializer(
        data={'league_id': 1,
              'game': {'home_user_id': 1, 'away_user_id': 2,
                       'home_team_id': 1, 'away_team_id': 1, 'home_score': 5,
                       'away_score': 3, 'penalty_shootout': False,
                       'date_played': datetime.datetime.now(),
                       'status': 2}})
    g1.is_valid()
    g1.save()
    g2 = LeagueGameSerializer(
        data={'league_id': 1,
              'game': {'home_user_id': 1, 'away_user_id': 2,
                       'home_team_id': 1, 'away_team_id': 1, 'home_score': 3,
                       'away_score': 1, 'penalty_shootout': False,
                       'date_played': datetime.datetime.now(),
                       'status': 2}})
    g2.is_valid()
    g2.save()
