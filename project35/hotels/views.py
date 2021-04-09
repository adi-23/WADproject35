from django.shortcuts import render
from .models import Place,Hotel
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse


class NewForm(forms.Form):
    hotelName          =forms.CharField(label="Hotel Name",max_length=50)
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


def add(request):
        if request.method=="POST":
                form=NewForm(request.POST)

                k=0

                for place in Place.objects.all():
                    if place.place_name==form['hotelPlace'].value():
                        k=1
                        obj=place
                        break
                if k==0:
                    obj = Place(place_name=form['hotelPlace'].value())
                    obj.save()



                hotelObj=Hotel(hotel_name=form['hotelName'].value(),hotel_address=form['hotelAddress'].value(),
                hotel_hasACrooms=form['hotelACrooms'].value(),hotel_place=obj,hotel_contactinfo=form['hotelContactinfo'].value())
                hotelObj.save()
                return render(request, "hotels/redir.html")


        else:
                return render(request, "hotels/add.html",{
            "form":NewForm()
        })
