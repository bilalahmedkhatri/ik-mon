from rest_framework import serializers
from accounts.models import MainUser


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'

