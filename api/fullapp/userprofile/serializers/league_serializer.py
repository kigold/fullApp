from rest_framework import serializers
from ..models import League


class LeagueSerializer(serializers.ModelSerializer):
    season = serializers.IntegerField()
    title = serializers.CharField()
    is_two_leg = serializers.BooleanField()

    class Meta:
        model = League
        fields = '__all__'
