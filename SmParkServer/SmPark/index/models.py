from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ParkingLot(models.Model):
    addr = models.CharField(unique=True,max_length = len("0x11aad4f50b2d1173b3dfb00ec14cb199f9374b6a"))
    info = models.TextField(blank=True, null=True, default="")
    state = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10,decimal_places=3,blank=True, null=True, default=0)
    location = models.CharField(max_length = 140,blank=True, null=True, default="")
    carId = models.CharField(max_length=20,blank=True, null=True, default="")
    hrs = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True, default=0)
class PL_User(models.Model):
    userIndex = models.CharField(unique=True,max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=3,blank=True, null=True, default=0)
                            
