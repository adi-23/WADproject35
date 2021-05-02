from django.shortcuts import render
from django.http import HttpResponse
from shops.models import Shop
from django.template import loader
from django import forms
from .filters import ShopFilter
from authentication.models import User,serviceprovider

# Create your views here.

class ShopForm(forms.ModelForm):
    
    #shopowner=forms.Charfield(label='enter you user name',max_length=50,display=None)
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

def addshop(request,user_id):

    # if request.method=="POST":
    #     shopform=ShopForm(request.POST)
    #     shopform.shop_owner_id=user_id
    #     if shopform.is_valid():
            
    #         shopform.save()
    # else:

    user=User.objects.get(id=user_id)
    shop_sp=serviceprovider.objects.get(user=user)
    if Shop.objects.filter(shop_owner=shop_sp).exists():
        #shop_sp=serviceprovider.objects.get(user=user)
        shop_instance=Shop.objects.get(shop_owner=shop_sp)
        # shopform=shopform(request,instance=shop_instance)
        # if shopform.is_valid():
        #     shopform.save()
        #     return render(request,"shops/shops.html")
        return render(request, 'shops/shops.html', context={'shop': shop_instance})
    else:
        
        shopform=ShopForm(initial={'shop_owner': serviceprovider.objects.get(user=user)})
       
        return render(request, 'shops/shopadding.html',{'form': shopform})


def shops(request):
    s_list=Shop.objects.all()
    s = ShopFilter(request.GET,queryset=s_list)

    return render(request,'shops/shops_list.html',{'filter': s,'hotels': s_list})




def editshops(request,user_id):
    
    shop_display=Shop.objects.filter(shop_owner_id=user_id)
    # shop_form=ShopForm(instance=shop_display)
    # if request.method == 'POST':
    #     shop_form= ShopForm(request.POST,instance=shop_display)
    #     if shop_form.is_valid():
    #         shop_form.save()
    #         return redirect('/')
    # context={'shop_form': shop_form}
    # return render(request,'shops/shopsedit.html',context)
    context={'shop': shop_display}
    return render(request,'shops/shopsedit.html',context)

