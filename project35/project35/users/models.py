from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Serviceusers(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    #phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
 
class Serviceproviders(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    
    #phone_number = models.CharField(max_length=20)
    shopname = models.CharField(max_length=20)


