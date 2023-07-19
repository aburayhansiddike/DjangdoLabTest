from django.shortcuts import render
from rest_framework import generics
from CatApp.models import CatShop
from CatApp.serializers import CatShopSerializer


# Create your views here.


class CatList(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer


class CatDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer

