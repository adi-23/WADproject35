from django.db import models
from authentication.models import serviceprovider,User
from django.urls import reverse
# Create your models here.
class Place(models.Model):
    place_name=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.place_name

class Hotel(models.Model):
    hotel_name          =models.CharField(max_length=50)
    hotel_address       =models.CharField(max_length=100)
    hotel_hasACrooms    =models.BooleanField(default=False)
    hotel_owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    hotel_place         =models.ForeignKey(Place,on_delete=models.CASCADE)
    hotel_contactinfo   =models.CharField(max_length=10)
    hotel_img           =models.ImageField(upload_to='pics/')
    
    def get_absolute_url(self):
         return reverse("hotel_detail", kwargs={"pk": self.pk})