from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Serviceusers,Serviceproviders

class ServiceusersSignUpForm(UserCreationForm):
#    first_name = forms.CharField(required=True)
#    last_name = forms.CharField(required=True)
#   phone_number = forms.CharField(required=True)
#    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        user.save()
        serviceusers = Serviceusers.objects.create(user=user)
        #customer.phone_number=self.cleaned_data.get('phone_number')
        #customer.location=self.cleaned_data.get('location')
        serviceusers.save()
        return user

class ServiceproviderSignUpForm(UserCreationForm):
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)
    #phone_number = forms.CharField(required=True)
    #designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        user.save()
        serviceproviders = Serviceproviders.objects.create(user=user)
        #employee.phone_number=self.cleaned_data.get('phone_number')
        #employee.designation=self.cleaned_data.get('designation')
        serviceproviders.save()
        return user
