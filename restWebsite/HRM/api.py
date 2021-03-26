from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from .serializers import *
from HRM.models import Users
from rest_framework import viewsets
from rest_framework import generics


class UserList(APIView):
    queryset = Users.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.queryset()
        serializer = UsersSerializer(queryset, many=True)
        return response(serializer.data)