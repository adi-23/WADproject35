from django.shortcuts import render,HttpResponse,redirect
from .models import Restaurant
from hotels.models import Place
from authentication.models import serviceprovider,User
from django import forms
from .filters import RestaurantFilter
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    UpdateView,
)


# Create your views here.
class RestaurantDetailView(DetailView):
    model=Restaurant


class RestaurantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Restaurant
    fields=['resta_name','has_AC','has_delivery','has_parking','restaurant_type','resta_img','resta_contact','resta_place','resta_address']

    def form_valid(self, form):
        if self.request.user.is_serviceprovider :
            form.instance.resta_owner= self.request.user
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the restaurant')

    def test_func(self):
        restauarnt =self.get_object()
        if self.request.user == restauarnt.resta_owner:
            return True
        return False


class RestaurantForm(forms.ModelForm):
    
    class Meta:
        model=Restaurant
        fields=["resta_name",
                "has_AC",
                "has_delivery",
                "has_parking",
                "resta_contact",
                "resta_img",
                "restaurant_type",
                "resta_address",
                "resta_place"]
        labels={
                'resta_name':"Enter restaurant name",
                'has_AC':"AC",
                'has_delivery':"Delivery",
                'has_parking':"Parking",
                'resta_contact':"Contact number",
                'resta_img':"restaurant image",
                'restaurant_type':"Veg,NonVeg,Both",
                'resta_address':"Address",
                'resta_place':"Place"
        }
        




def resta_view(request,user_id):
         if request.method=="POST":
                form=RestaurantForm(request.POST,request.FILES)

                k=0


                obj=Place.objects.get(id=form['resta_place'].value())
                user=User.objects.get(id=user_id)
                restaObj=Restaurant(resta_owner=user,
                                    resta_name=form['resta_name'].value(),
                                    has_AC=form['has_AC'].value(),
                                    has_delivery=form['has_delivery'].value(),
                                    has_parking=form['has_parking'].value(),
                                    resta_address=form['resta_address'].value(),
                                    resta_place=obj,
                                    resta_img=form['resta_img'].value(),
                                    restaurant_type=form['restaurant_type'].value(),
                                    resta_contact=form['resta_contact'].value())
                restaObj.save()
                return render(request,"hotels/redir.html",context={'restaurant': restaObj})


         else:
            if (Restaurant.objects.filter(resta_owner_id=user_id).first()) is not None:
                temp = Restaurant.objects.filter(resta_owner_id=user_id).first()
                i=temp.id
                url = '/restaurants/restaurant/{}/'.format(i)
                return redirect(url)
        
            else:
                form= RestaurantForm()
                return render(request,'restaurants/restaurant_form.html',{'form':form})


            
        
def restaurant(request):
    places=Place.objects.all()
    return render(request,'restaurants/rest1.html',{'Place':places})




def search(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    rest_info= Restaurant.objects.filter(resta_place_id=iid)
    p = Place.objects.filter(id=iid)
    context={'restinfo': rest_info, }
    return render(request,"restaurants/rest1.html",{
    'Place':Place.objects.all(),
    'Restaurants':rest_info,'place_id': iid

    })




def RestaurantListview(request,place_id):
    
    place=Place.objects.get(id=place_id)
    h_list=Restaurant.objects.filter(resta_place=place)
    h = RestaurantFilter(request.GET,queryset=h_list)

    return render(request,'restaurants/restaurant_list.html',{'filter': h,'restaurants': h_list,'place': place})


def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")


def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')