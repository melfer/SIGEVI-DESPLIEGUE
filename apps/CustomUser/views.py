from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.permissions import isAuth
class UserDataAPIView(APIView):
    permission_classes = [isAuth]
    def get_user(self, username):
        return get_object_or_404(CustomUser, user=username)
    
    def get(self,request):
        data = self.get_user(request.user.username)
        serializer = DataSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        dataCopy = request.data.copy()
        dataCopy['user'] = request.user.username
        serializer = DataSerializer(data=dataCopy)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data = self.get_user(request.user.username)
        dataCopy = request.data.copy()
        dataCopy['user'] = request.user.username
        serializer = DataSerializer(data,data=dataCopy)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)