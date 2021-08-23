from django.db import models
from django.contrib import admin

# Create your models here.
class DataHarian(models.Model):
    tanggal = models.DateField(blank=False, null=False, unique=True)
    kumulatif = models.IntegerField(default=0)
    sembuh = models.IntegerField(default=0)
    dalam_perawatan = models.IntegerField(default=0)
    meninggal = models.IntegerField(default=0)

    @admin.display(ordering='tanggal')

    def __str__(self):
        return str(self.tanggal)

class DataPerKecamatan(models.Model):
    tanggal = models.DateField(blank=False, null=False, unique=True)
    sagulung = models.IntegerField(default=0)
    bulang = models.IntegerField(default=0)
    batu_aji = models.IntegerField(default=0)
    belakang_padang = models.IntegerField(default=0)
    sekupang = models.IntegerField(default=0)
    lubuk_baja = models.IntegerField(default=0)
    batu_ampar = models.IntegerField(default=0)
    bengkong = models.IntegerField(default=0)
    nongsa = models.IntegerField(default=0)
    batam_kota = models.IntegerField(default=0)
    galang = models.IntegerField(default=0)
    sei_beduk = models.IntegerField(default=0)

    @admin.display(ordering='tanggal')

    def __str__(self):
        return str(self.tanggal)