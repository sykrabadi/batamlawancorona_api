from django.shortcuts import render
from rest_framework import generics
from .serializers import DataHarianSerializer
from .models import DataHarian

# Create your views here.
class DataHarianList(generics.ListCreateAPIView):
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer

class DataHarianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer