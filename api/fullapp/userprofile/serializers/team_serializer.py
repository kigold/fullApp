from rest_framework import serializers
from ..models import Team


class TeamSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)

    class Meta:
        model = Team
        fields = '__all__'
