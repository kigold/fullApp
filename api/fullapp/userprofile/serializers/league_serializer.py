from rest_framework import serializers
from ..models import League


class LeagueSerializer(serializers.ModelSerializer):
    season = serializers.IntegerField()
    title = serializers.CharField()

    class Meta:
        model = League
        fields = '__all__'
