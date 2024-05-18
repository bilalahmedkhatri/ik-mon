from django.urls import path, include

# DRF
from rest_framework import routers

# views control
from .views import UserViewSet, DailyViewMainData, save_data, SnippetList


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('us', include('rest_framework.urls', namespace='user_api')),

    # Testing api user
    # path('', ViewUserMonitor.as_view()),
    path('main/<int:pk>', DailyViewMainData.as_view()),
    path('main/', DailyViewMainData.as_view()),
    path('data', save_data),
    path('list', SnippetList.as_view()),
]
