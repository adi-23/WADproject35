from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,serviceprovider,serviceuser

class ServiceUserSignUpForm(UserCreationForm):  #class based form for creation of user(serviceuser) in registration
    Email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic  #if all fields are correct then create the user else stop the creation of user(i.e atomic)
    def save(self):
        user = super().save(commit=False)
        user.is_serviceuser = True
        user.is_staff=True
        user.save()
        s= serviceuser.objects.create(user=user)
        s.Email=self.cleaned_data.get('Email')
        s.save()
        return user


class ServiceProviderSignUpForm(UserCreationForm):      #class based form for creation of user(serviceprovider) in registration


    class Meta(UserCreationForm.Meta):
        model = User
                                 
    @transaction.atomic  #if all fields are correct then create the user else stop the creation of user(i.e atomic)
    def save(self):
        user = super().save(commit=False)
        user.is_serviceprovider = True
        user.is_staff=True
        user.save()
        o= serviceprovider.objects.create(user=user)
        o.choice=self.cleaned_data.get('choice')
        o.save()
        return user
