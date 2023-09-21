from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views as v
from djoser.views import UserViewSet

urlpatterns = [
    path('me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),
    path('me/info/', v.UserDataAPIView.as_view()),
]
