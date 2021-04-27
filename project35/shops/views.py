from django.shortcuts import render
from django.http import HttpResponse
from shops.models import Shop
from django.template import loader
from django import forms
from .filters import ShopFilter

# Create your views here.

class ShopForm(forms.ModelForm):
    
    # shopowner=forms.Charfield(label='enter you user name',max_length=50)
    # shopname=forms.CharField(label='shopname',max_length=25)
    # shopaddress=forms.CharField(label='shopaddress',max_length=100)
    # shopcontactinfo=forms.CharField(label='shopcontact',max_length=10)
    # shopplace=forms.Charfield(label='shopplace',max_length=30)
    class Meta:
        model=Shop
        fields=["shop_owner","shop_name","shop_address","shop_contactinfo","shop_place","shop_itemtype"]
        labels={'shop_owner': "enter your username",
        'shop_name': "enter shopname",
        'shop_address': "address",
        'shop_contactinfo': "contact",
        'shop_place': "place",
        'shop_itemtype': "sellingtype"}

def addshop(request):
    if request.method=="POST":
        shopform=ShopForm(request.POST)
        if shopform.is_valid():
            shopform.save()
    else:
        shopform=ShopForm()
    return render(request, 'shops/shopadding.html',{'form': shopform})


def shops(request):
    s_list=Shop.objects.all()
    s = ShopFilter(request.GET,queryset=s_list)

    return render(request,'shops/shops_list.html',{'filter': s,'hotels': s_list})


