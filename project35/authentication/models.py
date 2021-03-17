from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_serviceuser = models.BooleanField(default=False)
    is_serviceprovider = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)

class serviceuser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Email = models.EmailField(max_length=254)

class serviceprovider(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    business_choices = [('SH','Shops'),('HS','Hostels'),('RS','Restaurents'),('HO','Hospitals'),('SM','Shopping malls'),('CH','Cinema halls'),('TS','Tourism')]
    choice= models.CharField(max_length=2,choices=business_choices)
    #choice = models.CharField(max_length=20)


