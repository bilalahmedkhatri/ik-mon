from rest_framework import serializers
from accounts.models import MainCustomUser


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCustomUser
        fields = '__all__'


class MainUserSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCustomUser
        fields = ['last_name']
