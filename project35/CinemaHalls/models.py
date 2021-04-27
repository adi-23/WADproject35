from django.db import models
from hotels.models import Place
from django.core.validators import MinLengthValidator

class CinemaHall(models.Model):
    cinemahall_name          =models.CharField(max_length=50)
    seats                    =models.CharField(max_length=5)
    timing                   =models.CharField(max_length=100)
    cinemahall_address       =models.CharField(max_length=100)
    cinemahall_place         =models.ForeignKey(Place,on_delete=models.CASCADE)
    cinemahall_contactinfo   =models.CharField(max_length=10,validators=[MinLengthValidator(10)])

    




