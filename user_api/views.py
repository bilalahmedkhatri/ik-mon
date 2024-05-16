from rest_framework import viewsets
from rest_framework.response import Response
# from django.contrib.auth.models import User
from accounts.models import MainUser
from .serializer import UserSerializer, UserModelSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions, authentication, generics, status
from user_api.models import UserMonitor, Category


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
    queryset = UserMonitor.objects.all()
    serializer_class = UserModelSerializer
    # authentication_classes = [authentication.authenticates]


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
