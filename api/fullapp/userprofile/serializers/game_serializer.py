from rest_framework import serializers
from ..models import Game
from . import ProfileSerializer, TeamSerializer


class GameSerializer(serializers.ModelSerializer):
    away_user = ProfileSerializer(read_only=True)
    away_user_id = serializers.IntegerField(write_only=True)
    home_user = ProfileSerializer(read_only=True)
    home_user_id = serializers.IntegerField(write_only=True)
    away_score = serializers.IntegerField(required=False)
    home_score = serializers.IntegerField(required=False)
    home_team = TeamSerializer(read_only=True)
    home_team_id = serializers.IntegerField(write_only=True)
    away_team = TeamSerializer(read_only=True)
    away_team_id = serializers.IntegerField(write_only=True)
    penalty_shootout = serializers.BooleanField(required=False)
    date_played = serializers.DateTimeField(required=False)
    status = serializers.IntegerField()

    class Meta:
        model = Game
        fields = '__all__'

    def validate_for_played_game(self):
        data = self.initial_data
        required_fields = ['home_score', 'away_score',
                           'penalty_shootout', 'date_played']
        errors = []
        for field in required_fields:
            if field not in data or data[field] is None:
                errors.append(field + " is a required field")
        if len(errors) > 0:
            raise serializers.ValidationError(" | ".join(errors))
