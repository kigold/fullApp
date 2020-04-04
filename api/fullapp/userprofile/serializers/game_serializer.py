from rest_framework import serializers
from ..models import Game
from . import ProfileSerializer, TeamSerializer


class GameSerializer(serializers.ModelSerializer):
    away_user = ProfileSerializer()
    home_user = ProfileSerializer()
    away_score = serializers.IntegerField()
    home_score = serializers.IntegerField()
    home_team = TeamSerializer()
    away_team = TeamSerializer()
    penalty_shootout = serializers.BooleanField()
    date_played = serializers.DateTimeField()

    class Meta:
        model = Game
        fields = '__all__'
