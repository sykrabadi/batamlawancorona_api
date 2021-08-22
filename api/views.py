from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import DataHarianSerializer, DataPerKecamatanSerializer
from .models import DataHarian, DataPerKecamatan
from api import serializers

# Create your views here.
class DataHarianList(generics.ListAPIView):
    """
    Retrieve all daily cases
    """
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataHarianDetail(generics.RetrieveAPIView):
    """
    Retrieve based on specified date. Date format should be yyyy-mm-dd
    """
    lookup_field = 'tanggal'
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataPerKecamatanList(generics.ListAPIView):
    """
    Get/Retrieve daily cases (kasus harian) across all subdistrict of Batam
    """
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataPerKecamatanDetail(generics.RetrieveAPIView):
    """
    Get/Retrieve daily cases (kasus harian) across all subdistrict of Batam based on specified date. Date format should be yyyy-mm-dd
    """
    lookup_field = 'tanggal'
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]