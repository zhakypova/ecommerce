from django.shortcuts import render
from rest_framework import viewsets, views, generics, mixins
from .models import Profile
from .serializers import SenderRegisterSerializer, BuyerRegisterSerializer



class SenderCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = SenderRegisterSerializer


class BuyerCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = BuyerRegisterSerializer



