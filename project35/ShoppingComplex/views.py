from django.shortcuts import render,redirect
from hotels.models import Place
from authentication.models import serviceprovider
from .models import ShoppingComplex
from .forms import ShoppingComplexForm
# Create your views here.


def search(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    shopping_info= ShoppingComplex.objects.filter(shoppingcomplex_place_id=iid)
    p = Place.objects.filter(id=iid)
    context={'shoppinginfo': shopping_info, }
    return render(request,"ShoppingComplex/shopping.html",{
    'Place':Place.objects.all(),
    'shoppingMalls':shopping_info,'place':p

    })





def form_view(request,user_id):
    if request.method == "POST":
        form=ShoppingComplexForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places:
            if form['place'].value() == place.place_name:
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['place'].value())
            obj.save()
        h_sp=serviceprovider.objects.get(user_id=user_id)
        shopping = ShoppingComplex(shoppingcomplex_sp=h_sp,shoppingcomplex_hasFloors=form['floors'].value(),shoppingcomplex_name=form['name'].value(),shoppingcomplex_image=form['image'].value(),shoppingcomplex_place=obj,shoppingcomplex_address=form['address'].value(),shoppingcomplex_contactinfo=form['Contactinfo'].value())
        shopping.save()
        return render(request,'authentication/Serviceuserhomepage.html')
    else:
        form= ShoppingComplexForm()
        return render(request,'ShoppingComplex/form.html',{'form':form})


def shoppingcomplex(request):
    places=Place.objects.all()
    return render(request,'ShoppingComplex/shopping.html',{'Place':places})
