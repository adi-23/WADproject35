from django import forms

class ShoppingComplexForm(forms.Form):
    name=forms.CharField(label="Enter shopping complex name",max_length=100)
    image= forms.ImageField(label="Upload shopping complex photo")
    address= forms.CharField(label="Enter shopping complex address",max_length=100)
    floors = forms.CharField(label="No.of floors in mall",max_length=100)
    place = forms.CharField(label="Enter the place",max_length=50)
    Contactinfo= forms.CharField(label="Enter contact info",max_length=10)
