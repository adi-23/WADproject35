from django.db import models
from hotels.models import Place
from django.core.validators import MinLengthValidator
from authentication.models import User,serviceprovider
from django.urls import reverse


# Create your models here.
class Hospital(models.Model):
    hospital_name=models.CharField(max_length=100)
    doctors = models.CharField(max_length=100)
    hospital_image=models.ImageField(upload_to='pics/')
    hospital_place=models.ForeignKey(Place,on_delete=models.CASCADE)
    hospital_address=models.CharField(max_length=100)
    hospital_contactinfo = models.CharField(max_length=10,validators=[MinLengthValidator(10)])
    hospital_sp=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
         return reverse("hospital_detail", kwargs={"pk": self.pk})