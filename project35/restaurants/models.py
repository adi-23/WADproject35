

# Create your models here.
from django.db import models
from authentication.models import serviceprovider 
from hotels.models import Place
from hotels.models import Place
     

class Restaurant(models.Model):
   resta_name=models.CharField(max_length=50)  
   has_AC=models.BooleanField(default=False)
   has_delivery=models.BooleanField(default=False)
   has_parking=models.BooleanField(default=False)
   resta_contact=models.CharField(max_length=10)
   resta_address=models.CharField(max_length=150)
   VEG_NONVEG=(('Veg'),('NonVeg'),('Veg&NonVeg'),)
   resta_owner=models.ForeignKey(serviceprovider,on_delete=models.CASCADE)    
   resta_place=models.ForeignKey(Place,on_delete=models.CASCADE)

class Menu(models.Model):
   food_item=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
   fooditem_name=models.CharField(max_length=20)
   food_type=models.CharField(max_length=10)
   food_cost=models.IntegerField()
    
def _str_(self):
   return self.resta_name