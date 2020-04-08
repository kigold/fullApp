from rest_framework import serializers
from ..models import Profile, User
from . import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # first_name = serializers.CharField(read_only=True)
    # last_name = serializers.CharField()
    # password = serializers.CharField()
    fav_team_id = serializers.IntegerField()
    nick_name = serializers.CharField(max_length=50)
    points = serializers.IntegerField()
    # email = serializers.EmailField()
    # is_staff = serializers.BooleanField()
    # is_active = serializers.BooleanField()

    class Meta:
        model = Profile
        fields = ["nick_name", "points", "fav_team_id", 'user']

    def create(self, validated_data):
        user_serializer = UserSerializer(data=validated_data['user'])
        user_serializer.is_valid()
        user = user_serializer.save()

        # return super(ProfileSerializer, self).create(validated_data)
        validated_data['user'] = user
        profile = Profile.objects.create(**validated_data)
        return profile

    def update(self, instance, validated_data):
        user_serializer = UserSerializer(instance.user,
                                         data=validated_data['user'],
                                         partial=True)
        user_serializer.is_valid()
        user = user_serializer.save()

        del validated_data['user']
        profile = super().update(instance, validated_data)
        return profile
