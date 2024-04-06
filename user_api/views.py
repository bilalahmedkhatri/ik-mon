from rest_framework import viewsets
from rest_framework.response import Response
# from django.contrib.auth.models import User
from accounts.models import MainUser
from .serializer import UserSerializer, UserModelSerializer
from rest_framework.views import APIView
from rest_framework import permissions, authentication, generics
from user_api.models import UserMonitor


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    serializer_class = UserSerializer


class ViewUserMonitor(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usermodel = UserMonitor.objects.all()
        serializer = UserSerializer(usermodel, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     print("ss", request.data)
    #     return Response({'message': 'message is recieved'})


class ViewMainData(generics.ListAPIView):
    queryset = UserMonitor  .objects.all()
    serializer_class = UserModelSerializer
    # authentication_classes = [authentication.authenticates]
