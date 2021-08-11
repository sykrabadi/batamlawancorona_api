from django.contrib import admin
from .models import DataHarian, DataPerKecamatan

# Register your models here.
class DataHarianAdmin(admin.ModelAdmin):
    list_display = ('tanggal' ,'kumulatif', 'sembuh', 'dalam_perawatan', 'meninggal',)
    list_filter = ('tanggal',)

class DataPerKecamatanAdmin(admin.ModelAdmin):
    list_display = ('tanggal' ,'sagulung', 'bulang', 'batu_aji', 'belakang_padang', 'sekupang', 'lubuk_baja', 'batu_ampar', 'bengkong', 'nongsa', 'batam_kota', 'galang', 'sei_beduk',)

admin.site.register(DataPerKecamatan, DataPerKecamatanAdmin)
admin.site.register(DataHarian, DataHarianAdmin)