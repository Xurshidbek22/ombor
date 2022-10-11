from django.db import models
from userapp.models import Sotuvchi

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    miqdor = models.PositiveIntegerField()
    brend = models.CharField(max_length=50)
    kelgan_sana = models.DateField()
    olchov = models.CharField(max_length=255)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)

    def __str__(self):return f"{self.nom}, {self.brend}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    qarz = models.PositiveIntegerField(default=0)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)

    def __str__(self):return f"{self.ism} , {self.nom} ({self.manzil})"