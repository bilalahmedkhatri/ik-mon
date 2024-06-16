from django.contrib.auth.models import User
from accounts.models import MainUser
from user_api.models import UserMonitor, Category
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainUser
        fields = ['url', 'username', 'email', 'is_staff']


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMonitor
        fields = ['user_name', 'verification_code', 'ip_address',
                  'image_thumpnail', 'videos', 'os', 'date_create', 'date_update']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# Daily Monitoring
class DailyUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMonitor
        # fields = '__all__'
        fields = ("user_name", "video_url", "thumb_url", "verification_code", "ip_address",
                  "image_thumpnail", "videos", "os", "date_create", "live_status")
        # fields = ("user_name", "video_url", "verification_code", "ip_address",
        #           "image_thumpnail", "videos", "os", "date_create")


class StatusDailyUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMonitor
        fields = ("live_status")
