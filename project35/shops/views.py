from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shops.models import Shop
from django.template import loader
from hotels.models import Place
from django import forms
from .filters import ShopFilter
from authentication.models import User,serviceprovider


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

    
    shop_sp=serviceprovider.objects.get(user_id=user_id)
    print(shop_sp)
    if (Shop.objects.filter(shop_owner=shop_sp)) is not None:
        #shop_sp=serviceprovider.objects.get(user=user)
        shop_instance=Shop.objects.get(shop_owner=shop_sp)
        print(shop_instance) 
        shop_form=ShopForm(instance=shop_instance)
        if request.method=='POST':
            shiop_form=ShopForm(request.POST or None,instance=shop_instance)
            if shop_form.is_valid():
                shop_obj=shop_form.save()
                return render(request,"shops/shops.html")
            else:
                return render(request, 'shops/shopadding.html', context={'form': shop_form})
    else:
        print('else')
        shop_form=ShopForm(initial={'shop_owner': serviceprovider.objects.get(user_id=user_id)})
        if request.method=='POST':
            shop_form=ShopForm(request.POST or None,initial={'shop_owner': serviceprovider.objects.get(user_d=user_id)})
            if shop_form.is_valid():
                shopobj=shop_form(commit=False)
                shopobj.shop_owner=shop_sp
                shopobj.save()
                return render(request,'authentication/ServiceuserHompepage.html')
            else:
                return render(request,'shops/shopadding.html')
        else:
            return render(request,'shops/shopadding.html',{'form': shop_form})
       
            


def shops(request,place_id):
    place=Place.objects.get(id=place_id)
    s_list=Shop.objects.filter(shop_place=place)
    s = ShopFilter(request.GET,queryset=s_list)

    return render(request,'shops/shops_list.html',{'filter': s,'hotels': s_list})




def editshops(request,user_id):
    user=User.objects.get(id=user_id)
    sp_user=serviceprovider.objects.get(user=user)
    shop_display=Shop.objects.filter(shop_owner=sp_user)
    # shop_form=ShopForm(instance=shop_display)
    # if request.method == 'POST':
    #     shop_form= ShopForm(request.POST,instance=shop_display)
    #     if shop_form.is_valid():
    #         shop_form.save()
    #         return redirect('/')
    # context={'shop_form': shop_form}
    # return render(request,'shops/shopsedit.html',context)
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    #obj = get_object_or_404(Shop, id = id)
  
    # pass the object as instance in form
    form = ShopForm(request, instance = shop_display)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/"+id)
  
    # add form dictionary to context
    context["form"] = form
  
    return render(request, "shops/shopsedit.html", context)
    # context={'shop': shop_display}
    # return render(request,'shops/shopsedit.html',context)

