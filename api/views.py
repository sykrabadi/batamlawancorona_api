from django.shortcuts import render
from rest_framework import generics
from .serializers import DataHarianSerializer, DataPerKecamatanSerializer
from .models import DataHarian, DataPerKecamatan
from api import serializers

# Create your views here.
class DataHarianList(generics.ListCreateAPIView):
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer

class DataHarianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer

class DataPerKecamatanList(generics.ListCreateAPIView):
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer

class DataPerKecamatanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer