from rest_framework import serializers
from .models import DataHarian

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