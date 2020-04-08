from rest_framework import serializers
from ..models import Game
from . import ProfileSerializer, TeamSerializer


class GameSerializer(serializers.ModelSerializer):
    away_user = ProfileSerializer()
    away_user_id = serializers.IntegerField(write_only=True)
    home_user = ProfileSerializer()
    home_user_id = serializers.IntegerField(write_only=True)
    away_score = serializers.IntegerField()
    home_score = serializers.IntegerField()
    home_team = TeamSerializer()
    home_team_id = serializers.IntegerField(write_only=True)
    away_team = TeamSerializer()
    away_team_id = serializers.IntegerField(write_only=True)
    penalty_shootout = serializers.BooleanField()
    date_played = serializers.DateTimeField()

    class Meta:
        model = Game
        fields = '__all__'
