from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    # Profile = serializers.PrimaryKeyRelatedField(many=False)
    # password = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    # is_staff = serializers.BooleanField()
    # is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
