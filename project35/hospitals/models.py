from django.db import models
from hotels.models import Place
from django.core.validators import MinLengthValidator


# Create your models here.
class Hospital(models.Model):
    hospital_name=models.CharField(max_length=100)
    doctors = models.CharField(max_length=100)
    hospital_image=models.ImageField(upload_to='pics/')
    hospital_place=models.ForeignKey(Place,on_delete=models.CASCADE)
    hospital_address=models.CharField(max_length=100)
    hospital_contactinfo = models.CharField(max_length=10,validators=[MinLengthValidator(10)])