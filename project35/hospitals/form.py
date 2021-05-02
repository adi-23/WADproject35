from django import forms
from django.core.validators import MinLengthValidator


class HospitalForm(forms.Form):

    hospitalName=forms.CharField(label="Enter hospital name",max_length=100)
    hospitalImage= forms.ImageField(label="Upload hospital photo")
    hospitalAddress= forms.CharField(label="Enter hospital address",max_length=100)
    doctors = forms.CharField(label="Doctor names working in the hospital",max_length=100)
    hospitalPlace = forms.CharField(label="Enter the place",max_length=50)
    hospitalContactinfo= forms.CharField(label="Enter contact info",max_length=10)