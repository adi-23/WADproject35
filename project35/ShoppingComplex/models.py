from django.db import models
from hotels.models import Place
from authentication.models import User,serviceprovider
from django.urls import reverse
# Create your models here.

class ShoppingComplex(models.Model):
    shoppingcomplex_name          =models.CharField(max_length=50)
    shoppingcomplex_address       =models.CharField(max_length=100)
    shoppingcomplex_hasFloors    =models.CharField(max_length=2)
    shoppingcomplex_place         =models.ForeignKey(Place,on_delete=models.CASCADE)
    shoppingcomplex_contactinfo   =models.CharField(max_length=10)
    shoppingcomplex_image=models.ImageField(upload_to='pics/')
    shoppingcomplex_sp=models.ForeignKey(User,on_delete=models.CASCADE)
    def get_absolute_url(self):
         return reverse("shoppingcomplex_detail", kwargs={"pk": self.pk})
