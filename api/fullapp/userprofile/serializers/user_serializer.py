from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    # Profile = serializers.PrimaryKeyRelatedField(many=False)
    # password = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=50, read_only=True)
    email = serializers.EmailField()
    # is_staff = serializers.BooleanField()
    # is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    '''def create(self, validated_data):
        print(")))))))))))))))))SERIALIZER User((((((((((((((((((((((")
        print(validated_data)
        user_data = {'email': validated_data['email']}        
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        print(")))))))))))))))))SERIALIZER USER((((((((((((((((((((((")
        print(user)
        profile = Profile(user.id, validated_data['email'],
                          validated_data['nick_name'],
                          validated_data['is_staff'])'''
