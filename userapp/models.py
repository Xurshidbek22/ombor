from django.contrib.auth.models import User
from django.db import models

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    user = models.ManyToManyField(User,null=True)

    def __str__(self):return self.ism