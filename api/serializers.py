from django.db import models
from rest_framework import serializers
from .models import DataHarian, DataPerKecamatan

class DataHarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataHarian
        fields = [
            'pk',
            'tanggal',
            'kumulatif',
            'sembuh',
            'dalam_perawatan',
            'meninggal',
        ]

class DataPerKecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPerKecamatan
        fields = [
            'pk',
            'tanggal',
            'sagulung', 
            'bulang', 
            'batu_aji', 
            'belakang_padang', 
            'sekupang', 
            'lubuk_baja', 
            'batu_ampar', 
            'bengkong', 
            'nongsa', 
            'batam_kota', 
            'galang', 
            'sei_beduk',
        ]