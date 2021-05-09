from django.shortcuts import render,redirect
from .models import Place,Hotel
from authentication.models import serviceprovider,User
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import HotelFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    UpdateView,
)


class NewForm(forms.Form):
    hotelName          =forms.CharField(label="Hotel Name",max_length=50)
    hotelImage         =forms.ImageField(label="Upload your hotel photo")
    hotelAddress       =forms.CharField(label="Hotel Address",max_length=100)
    hotelACrooms       =forms.BooleanField(label="AC",required=False)
    hotelPlace         =forms.CharField(label="Place",max_length=50)
    hotelContactinfo   =forms.CharField(label="Contact number",max_length=10)

# Create your views here.
# def hotels(request):
#     placeid = Place.objects.filter(place_name='palakollu')
#     hotels_info= Hotel.objects.filter(hotel_place = placeid.get(id=2))
#     context={'hotelsinfo': hotels_info, }
#     return render(request,"hotels/base.html",context)

class HotelDetailView(DetailView):
    model=Hotel


class HotelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Hotel
    fields=['hotel_name','hotel_img','hotel_hasACrooms','hotel_address','hotel_place','hotel_contactinfo']

    def form_valid(self, form):
        if self.request.user.is_serviceprovider :
            form.instance.hotel_owner = self.request.user
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the hotels')

    def test_func(self):
        hotel =self.get_object()
        if self.request.user == hotel.hotel_owner:
            return True
        return False








def hotels(request):

    return render(request,"hotels/hotel.html",{
    'Place':Place.objects.all()
    })

def index(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    hotels_info= Hotel.objects.filter(hotel_place=iid)
    context={'hotelsinfo': hotels_info, }
    return render(request,"hotels/hotel.html",{
    'Place':Place.objects.all(),
    'Hotel':hotels_info

    })


def add(request,user_id):
        if request.method=="POST":
                form=NewForm(request.POST,request.FILES)

                k=0

                for place in Place.objects.all():
                    if place.place_name==form['hotelPlace'].value():
                        k=1
                        obj=place
                        break
                if k==0:
                    obj = Place(place_name=form['hotelPlace'].value())
                    obj.save()
                
                
                hotel_sp=User.objects.get(id=user_id)
                hotelObj=Hotel(hotel_img=form['hotelImage'].value(),hotel_owner=hotel_sp,hotel_name=form['hotelName'].value(),hotel_address=form['hotelAddress'].value(),hotel_hasACrooms=form['hotelACrooms'].value(),hotel_place=obj,hotel_contactinfo=form['hotelContactinfo'].value())
                hotelObj.save()
                return render(request, "hotels/redir.html")


        else:

            if (Hotel.objects.filter(hotel_owner_id=user_id).first()) is not None:
                temp = Hotel.objects.filter(hotel_owner_id=user_id).first()
                i=temp.id
                url = '/hotels/hotel/{}/'.format(i)
                return redirect(url)
            else:
                    return render(request, "hotels/hotel_form.html",{
                "form":NewForm()
            })

def HotelListview(request,place_id):
    # model=Hotel
    # template_name='hotels/hotel_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
    
    place=Place.objects.get(id=place_id)
    h_list=Hotel.objects.filter(hotel_place=place)
    h = HotelFilter(request.GET,queryset=h_list)

    return render(request,'hotels/hotel_list.html',{'filter': h,'hotels': h_list})



def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")


def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')
