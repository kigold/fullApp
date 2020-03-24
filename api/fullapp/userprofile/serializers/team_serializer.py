from rest_framework import serializers
from ..models import Team


class TeamSerializer(serializers.ModelSerializer):
    # Id = serializers.IntegerField()
    Name = serializers.CharField(max_length=50)
    Country = serializers.CharField(max_length=50)

    class Meta:
        model = Team
        fields = '__all__'
