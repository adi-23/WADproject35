from django.db import models
from hotels.models import Place
from authentication.models import serviceprovider
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
    shop_owner=models.ForeignKey(serviceprovider,on_delete=models.CASCADE)
    shop_name=models.CharField(max_length=25)
    shop_address=models.CharField(max_length=100)
    shop_contactinfo=models.CharField(max_length=10)
    shop_place=models.ForeignKey(Place,on_delete=models.CASCADE)
    