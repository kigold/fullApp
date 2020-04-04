from rest_framework import serializers
from ..models import LeagueGame
from . import GameSerializer, LeagueSerializer


class LeagueGameSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    league = LeagueSerializer()

    class Meta:
        model = LeagueGame
        fields = '__all__'
