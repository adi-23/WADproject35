from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,serviceprovider,serviceuser

class ServiceUserSignUpForm(UserCreationForm):
    Email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_serviceuser = True
        user.is_staff=True
        user.save()
        s= serviceuser.objects.create(user=user)
        s.Email=self.cleaned_data.get('Email')
        s.save()
        return user


class ServiceProviderSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_serviceprovider = True
        user.is_staff=True
        user.save()
        o= serviceprovider.objects.create(user=user)
        o.choice=self.cleaned_data.get('choice')
        o.save()
        return user
