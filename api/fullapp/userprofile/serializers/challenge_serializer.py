from rest_framework import serializers
from django.db import transaction
from ..models import Challenge
from ..service import GameService
from . import ProfileSerializer, GameSerializer


class ChallengeSerializer(serializers.ModelSerializer):
    challenged = ProfileSerializer(read_only=True)
    challenged_id = serializers.IntegerField(required=True)
    challenger = ProfileSerializer(read_only=True)
    challenger_id = serializers.IntegerField(required=True)
    game = GameSerializer(required=True)
    game_id = serializers.IntegerField(required=False)
    proposed_date = serializers.DateTimeField(required=False)

    class Meta:
        model = Challenge
        fields = '__all__'

    def create(self, validated_data):
        try:
            with transaction.atomic():
                game_serializer = GameSerializer(data=validated_data['game'])
                if validated_data['game']['status']:
                    if validated_data['game']['status'] is 2:
                        game_serializer.validate_for_played_game()
                game_serializer.is_valid()
                game = game_serializer.save()
                validated_data['game_id'] = game.id
                game_data = validated_data.pop('game')
                challenge = Challenge.objects.create(**validated_data)
                if game_data['status'] is 2:
                    # Compute user points from game
                    GameService.compute_user_points(
                            game_data['home_user_id'],
                            game_data['away_user_id'],
                            game_data['home_score'],
                            game_data['away_score'])
                return challenge
        except Exception as e:
            raise serializers.ValidationError(
                detail=e)

    def update(self, instance, validated_data):
        if instance.game.status is 2:
            raise serializers.ValidationError(
                detail="Game already played cannot update")
        game_serializer = GameSerializer(instance.game,
                                         data=validated_data['game'],
                                         partial=True)
        game_serializer.is_valid()
        game = game_serializer.save()

        game_data = validated_data.pop('game')
        challenge = super().update(instance, validated_data)
        if game_data['status'] is 2:
            # Compute user points from game
            GameService.compute_user_points(
                    game_data['home_user_id'],
                    game_data['away_user_id'],
                    game_data['home_score'],
                    game_data['away_score'])
        return challenge
