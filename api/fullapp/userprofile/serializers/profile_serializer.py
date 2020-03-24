from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    fav_team_id = serializers.IntegerField()
    nick_name = serializers.CharField(max_length=50)
    points = serializers.IntegerField()
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()

    class Meta:
        model = Profile
        fields = ("fav_team_id", "nick_name", "points", "username",
                  "email", "password", "is_staff", "is_active")

    def create(self, validated_data):
        user = super(ProfileSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile(user.user_id, validated_data['email'],
                          validated_data['nick_name'],
                          validated_data['is_staff'])
