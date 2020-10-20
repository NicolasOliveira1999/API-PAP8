from django.shortcuts import render
from rest_framework import viewsets
from IOT.models import Lamp,Usuario,Hist
from IOT.serializer import LampSerializer,UsuarioSerializer,HistSerializer

class LampViewSet(viewsets.ModelViewSet):
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class HistViewSet(viewsets.ModelViewSet):
    queryset = Hist.objects.all()
    serializer_class = HistSerializer


