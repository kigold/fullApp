from rest_framework import serializers
from ..models import Challenge
from . import ProfileSerializer, GameSerializer


class ChallengeSerializer(serializers.ModelSerializer):
    challenged = ProfileSerializer()
    challenger = ProfileSerializer()
    game = GameSerializer()
    proposed_date = serializers.DateTimeField()

    class Meta:
        model = Challenge
        fields = '__all__'
