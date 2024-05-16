from rest_framework import serializers
from accounts.models import MainUser


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'


class MainUserSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['last_name']
        # fields = ["os_name"]
        # field = ["username", "os", "datetime"]
