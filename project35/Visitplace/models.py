from django.db import models
from hotels.models import Place


# Create your models here.

class Attractions(models.Model):
   attraction_name          = models.CharField(max_length=50, default='Attraction')
   attraction_type          = models.CharField(max_length=50, default='attracttion')
   attraction_place         = models.ForeignKey(Place,on_delete=models.CASCADE, default='1')
   attraction_description   = models.CharField(max_length=500, default='Place to visit')
   attraction_img           = models.ImageField(upload_to='Images/')





