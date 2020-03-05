from rest_framework import serializers
from ..model import Profile


class ProfileSerializer(serializers.ModelSerializer):
    fav_team_id = serializers.IntegerField()
    nick_name = serializers.CharField(max_length=50)
    point = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = ("fav_team_id", "nick_name", "points")