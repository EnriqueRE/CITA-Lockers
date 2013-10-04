from django.db import models

# Create your models here.
class LockerZone(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    occupied = models.CharField(max_length=200)
    free = models.CharField(max_length=200)

