from django.urls import path, include

# DRF
from rest_framework import routers

# views control
from .views import UserViewSet, ViewUserMonitor, ViewMainData


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('us', include('rest_framework.urls', namespace='user_api')),

    # Testing api user
    # path('', ViewUserMonitor.as_view()),
    path('<int:pk>', ViewUserMonitor.as_view()),
    path('main/', ViewMainData.as_view()),
]
