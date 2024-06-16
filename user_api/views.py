from rest_framework import viewsets
from rest_framework.response import Response
# from django.contrib.auth.models import User
from accounts.models import MainUser
from .serializer import UserSerializer, CategorySerializer, DailyUserModelSerializer, StatusDailyUserModelSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions, authentication, generics, status
from user_api.models import UserMonitor, Category
from django.db.models import Q
import datetime

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


class DailyViewMainData(APIView):

    def get(self, request, pk=None):
        current_date = datetime.date.today()
        get_all = UserMonitor.objects.filter(
            Q(date_create__gt=str(current_date.today())))
        serializer = DailyUserModelSerializer(get_all, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        gting_dt_4rm_client = DailyUserModelSerializer(data=request.data)
        if gting_dt_4rm_client.is_valid():
            gting_dt_4rm_client.save()
            return Response(gting_dt_4rm_client.data, status=status.HTTP_201_CREATED)
        return Response(gting_dt_4rm_client.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def daily_user_live_status(request):
    status = StatusDailyUserModelSerializer(request.data)
    if status.is_valid():
        return Response(status.data, status-status.HTTP_201_CREATED)
    return Response(status.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_data(request):
    ds = CategorySerializer(data=request.data)
    if ds.is_valid():
        ds.save()
        return Response(ds.data, status=status.HTTP_201_CREATED)
    return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
