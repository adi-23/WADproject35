from django import forms

class HotelForm(forms.Form):
    hotel_name          =forms.CharField(label="enter hotel name",max_length=50)
    hotel_address       =forms.CharField(label="enter the hotel address",max_length=100)
    hotel_hasACrooms    =forms.BooleanField(label="select option",default=False)
    hotel_contactinfo   =forms.CharField(label="enter mobile number",max_length=10)
    
    