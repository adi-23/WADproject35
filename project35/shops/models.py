from django.db import models
from hotels.models import Place
from django.urls import reverse
from authentication.models import serviceprovider,User
# Create your models here.
class Shop(models.Model):
    
    item_type=[
    ('HN','HomeNeeds'),
    ('ELE','Electrial'),
    ('STN','Stationary'),
    ('CLTH','Clothing'),
    ('BNKM','Banking and Money'),
    ('FAN','Fashion and jewlery'),
    ('SPRT','Sport'),
    ('FUN','Furniture')
    ]
    shop_itemtype=models.CharField(max_length=20,choices=item_type,default='HN')

    shop_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    shop_image=models.ImageField(upload_to='pics/')
    shop_name=models.CharField(max_length=25)
    shop_address=models.CharField(max_length=100)
    shop_contactinfo=models.CharField(max_length=10)
    shop_place=models.ForeignKey(Place,on_delete=models.CASCADE)

    def get_absolute_url(self):
         return reverse("shop_detail", kwargs={"pk": self.pk})
    