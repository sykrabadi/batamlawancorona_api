from django.db import models
from django.contrib import admin

# Create your models here.
class DataHarian(models.Model):
    tanggal = models.DateField(blank=False, null=False, unique=True)
    kumulatif = models.IntegerField(blank=True)
    sembuh = models.IntegerField(blank=True)
    dalam_perawatan = models.IntegerField(blank=True)
    meninggal = models.IntegerField(blank=True)

    @admin.display(ordering='tanggal')

    def __str__(self):
        return str(self.tanggal)

class DataPerKecamatan(models.Model):
    tanggal = models.DateField(blank=False, null=False, unique=True)
    sagulung = models.IntegerField(blank=True)
    bulang = models.IntegerField(blank=True)
    batu_aji = models.IntegerField(blank=True)
    belakang_padang = models.IntegerField(blank=True)
    sekupang = models.IntegerField(blank=True)
    lubuk_baja = models.IntegerField(blank=True)
    batu_ampar = models.IntegerField(blank=True)
    bengkong = models.IntegerField(blank=True)
    nongsa = models.IntegerField(blank=True)
    batam_kota = models.IntegerField(blank=True)
    galang = models.IntegerField(blank=True)
    sei_beduk = models.IntegerField(blank=True)
    transit = models.IntegerField(blank=True)

    @admin.display(ordering='tanggal')

    def __str__(self):
        return str(self.tanggal)