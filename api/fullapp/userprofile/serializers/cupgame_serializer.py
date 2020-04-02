from rest_framework import serializers
from ..models import CupGame
from . import GameSerializer, CupSerializer


class CupGameSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    cup = CupSerializer()
    stage = serializers.IntegerField()
    prev_game = GameSerializer()

    class Meta:
        model = CupGame
        fields = '__all__'
