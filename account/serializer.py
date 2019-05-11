from rest_framework import serializers
from .models import User, RentOutAHome


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = '__all__'


class RentOutAHomeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return RentOutAHome.objects.create(**validated_data)

    class Meta:
        model = RentOutAHome
        fields = '__all__'
