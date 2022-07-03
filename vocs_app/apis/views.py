from operator import mod
from django.shortcuts import render

# Create your views here.
from vocs import models
from .serializers import VocSerializer
from rest_framework import generics

class VocListCreateAPIView(generics.ListCreateAPIView):      #list and create object / get post
    queryset = models.Voc.objects.all()
    serializer_class = VocSerializer

class VocDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  #R.U.D object / get put patch delete
    queryset = models.Voc.objects.all()
    serializer_class = VocSerializer
