from django.contrib import admin
from .models import DataHarian

# Register your models here.
class DataHarianAdmin(admin.ModelAdmin):
    list_display = ('tanggal' ,'kumulatif', 'sembuh', 'dalam_perawatan', 'meninggal',)
    list_filter = ('tanggal',)

admin.site.register(DataHarian, DataHarianAdmin)