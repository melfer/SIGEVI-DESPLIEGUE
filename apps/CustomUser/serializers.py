from djoser.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class CustomUserSerializer(UserSerializer):
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'username',
                  'first_name', 'last_name', 'groups','is_superuser')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

