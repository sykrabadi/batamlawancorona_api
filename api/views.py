from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import DataHarianSerializer, DataPerKecamatanSerializer
from .models import DataHarian, DataPerKecamatan
from api import serializers

# Create your views here.
class DataHarianList(generics.ListAPIView):
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataHarianDetail(generics.RetrieveAPIView):
    lookup_field = 'tanggal'
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataPerKecamatanList(generics.ListAPIView):
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataPerKecamatanDetail(generics.RetrieveAPIView):
    lookup_field = 'tanggal'
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]