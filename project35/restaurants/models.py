# Create your models here.
from django.db import models
from authentication.models import serviceprovider 
from hotels.models import Place



class Restaurant(models.Model):
   resta_name=models.CharField(max_length=50)  
   has_AC=models.BooleanField(default=False)
   has_delivery=models.BooleanField(default=False)
   has_parking=models.BooleanField(default=False)
   resta_contact=models.CharField(max_length=10)
   resta_address=models.CharField(max_length=150)
   Veg_Nonveg=[('V','Veg'),('NV','NonVeg'),('V and NV','VegandNonVeg')]
   restaurant_type=models.CharField(max_length=10,choices=Veg_Nonveg,default='V and NV')
   resta_owner=models.ForeignKey(serviceprovider,on_delete=models.CASCADE)    
   resta_place=models.ForeignKey(Place,on_delete=models.CASCADE)

class Menu(models.Model):
   restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
   fooditem_name=models.CharField(max_length=20)
   vegornonveg=[('V','Veg'),('NV','NonVeg')]
   food_type=models.CharField(max_length=10,choices=vegornonveg)
   food_cost=models.IntegerField(default=0)
   
def _str_(self):
   return self.resta_name