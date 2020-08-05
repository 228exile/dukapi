# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Voisin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=True)
    phone = models.CharField(max_length=100, blank=False, null=True)
    adress = models.CharField(max_length=100, blank=False, null=True)
    about = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.name

class Favory(models.Model):
    id = models.AutoField(primary_key=True)
    id_voisin = models.IntegerField()
    Favory = models.ForeignKey(Voisin,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_voisin)
