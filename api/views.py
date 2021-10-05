from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .serializers import DataHarianSerializer, DataPerKecamatanSerializer
from .models import DataHarian, DataPerKecamatan
from .pagination import StandardResultsSetPagination
from api import serializers

# Create your views here.
class DataHarianList(generics.ListAPIView):
    """
    Retrieve all daily cases
    """
    queryset = DataHarian.objects.all()
    serializer_class = DataHarianSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['tanggal']
    ordering = ['-tanggal']

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
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['tanggal']
    ordering = ['-tanggal']

class DataPerKecamatanDetail(generics.RetrieveAPIView):
    """
    Get/Retrieve daily cases (kasus harian) across all subdistrict of Batam based on specified date. Date format should be yyyy-mm-dd
    """
    lookup_field = 'tanggal'
    queryset = DataPerKecamatan.objects.all()
    serializer_class = DataPerKecamatanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]