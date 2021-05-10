from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from shops.models import Shop
from django.template import loader
from hotels.models import Place
from django import forms
from .filters import ShopFilter
from authentication.models import User,serviceprovider
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    UpdateView,
)


class ShopForm(forms.ModelForm):
    
    #shopowner=forms.Charfield(label='enter you user name',max_length=50,display=None)
    # shopname=forms.CharField(label='shopname',max_length=25)
    # shopaddress=forms.CharField(label='shopaddress',max_length=100)
    # shopcontactinfo=forms.CharField(label='shopcontact',max_length=10)
    # shopplace=forms.Charfield(label='shopplace',max_length=30)
    class Meta:
        model=Shop
        fields=["shop_name","shop_image","shop_address","shop_contactinfo","shop_place","shop_itemtype"]
        labels={
        'shop_name': "enter shopname",
        'shop_address': "address",
        'shop_contactinfo': "contact",
        'shop_place': "place",
        'shop_itemtype': "sellingtype",
        'shop_image' : "Upload shop photo",
        }

class ShopDetailView(DetailView):
    model=Shop


class ShopUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Shop
    fields=['shop_itemtype','shop_image','shop_name','shop_address','shop_place','shop_contactinfo']

    def form_valid(self, form):
        if self.request.user.is_serviceprovider :
            form.instance.shop_owner = self.request.user
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the shop')

    def test_func(self):
        shop =self.get_object()
        if self.request.user == shop.shop_owner:
            return True
        return False


def form_view(request,user_id):
    if request.method == "POST":
        form=ShopForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        
        obj=Place.objects.get(id=form['shop_place'].value())
        shop_owner=User.objects.get(id=user_id)
        sp = Shop(shop_image=form['shop_image'].value(),shop_owner=shop_owner,shop_itemtype=form['shop_itemtype'].value(),shop_name=form['shop_name'].value(),shop_place=obj,shop_address=form['shop_address'].value(),shop_contactinfo=form['shop_contactinfo'].value())
        sp.save()
        return render(request,'hotels/redir.html')
    else:
        if (Shop.objects.filter(shop_owner_id=user_id).first()) is not None:
            temp = Shop.objects.filter(shop_owner_id=user_id).first()
            i=temp.id
            url = '/shops/shop/{}/'.format(i)
            return redirect(url)
        
        else:
            form= ShopForm()
            return render(request,'shops/shop_form.html',{'form':form})


def search(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    shop_info= Shop.objects.filter(shop_place_id=iid)
    p = Place.objects.filter(id=iid)
    context={'shopinfo': shop_info, }
    return render(request,"shops/shops.html",{
    'Place':Place.objects.all(),
    'shops':shop_info,'place':p,
    'place_id': iid

    })  

def shopcomplex(request):
    places=Place.objects.all()
    return render(request,'shops/shops.html',{'Place':places})
       
            


def shops(request,place_id):
    place=Place.objects.get(id=place_id)
    s_list=Shop.objects.filter(shop_place=place)
    s = ShopFilter(request.GET,queryset=s_list)

    return render(request,'shops/shops_list.html',{'filter': s,'hotels': s_list,'place':place})




def editshops(request,user_id):
    user=User.objects.get(id=user_id)
    sp_user=serviceprovider.objects.get(user=user)
    shop_display=Shop.objects.filter(shop_owner=sp_user)

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

