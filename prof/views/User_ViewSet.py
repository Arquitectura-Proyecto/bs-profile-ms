# User_ViewSet.py
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from ..models.User_model import User
from ..serializers.User_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_name')
    serializer_class = UserSerializer








