from rest_framework import serializers
from ..models import Cup


class CupSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Cup
        fields = '__all__'
