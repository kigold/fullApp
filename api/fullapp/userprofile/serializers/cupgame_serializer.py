from rest_framework import serializers
from django.urls import reverse
from django.db import transaction
from ..models import CupGame
from ..service import GameService
from . import GameSerializer, CupSerializer


class CupGameSerializer(serializers.ModelSerializer):
    game = GameSerializer(required=True)
    game_id = serializers.IntegerField(required=False)
    cup = CupSerializer(read_only=True)
    cup_id = serializers.IntegerField(write_only=True)
    stage = serializers.IntegerField()
    prev_game = GameSerializer(required=False)

    class Meta:
        model = CupGame
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
                game_data = validated_data['game']
                del validated_data['game']
                cupgame = CupGame.objects.create(**validated_data)
                if game_data['status'] is 2:
                    # Compute user points from game
                    GameService.compute_user_points(
                            game_data['home_user_id'],
                            game_data['away_user_id'],
                            game_data['home_score'],
                            game_data['away_score'])
                return cupgame
        except Exception as e:
            print("error creatng cup game")
            print
            raise Exception(e)