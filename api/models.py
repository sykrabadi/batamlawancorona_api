from django.db import models

# Create your models here.
class DataHarian(models.Model):
    tanggal = models.DateField(blank=False, null=False)
    kumulatif = models.IntegerField(default=0)
    sembuh = models.IntegerField(default=0)
    dalam_perawatan = models.IntegerField(default=0)
    meninggal = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tanggal)