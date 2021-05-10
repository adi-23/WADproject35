# Create your models here.
from django.db import models
from authentication.models import serviceprovider,User 
from hotels.models import Place
from django.urls import reverse



class Restaurant(models.Model):
   resta_name=models.CharField(max_length=50)  
   has_AC=models.BooleanField(default=False)
   has_delivery=models.BooleanField(default=False)
   has_parking=models.BooleanField(default=False)
   resta_contact=models.CharField(max_length=10)
   resta_address=models.CharField(max_length=150)
   Veg_Nonveg=[('V','Veg'),('NV','NonVeg'),('V and NV','VegandNonVeg')]
   restaurant_type=models.CharField(max_length=10,choices=Veg_Nonveg,default='V and NV')
   resta_owner=models.ForeignKey(User,on_delete=models.CASCADE)    
   resta_place=models.ForeignKey(Place,on_delete=models.CASCADE)
   resta_img = models.ImageField(upload_to='pics/')
   
   
   def get_absolute_url(self):
         return reverse("restaurant_detail", kwargs={"pk": self.pk})
   
def _str_(self):
   return self.resta_name