from django.shortcuts import render
from hotels.models import Place
from .models import CinemaHall
from .form import CinemaHallForm
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from authentication.models import serviceprovider
from .filters import CinemaHallFilter
# Create your views here.

# def form_view(request):
    
#     form = CinemaHallForm()
#     return  render(request,'CinemaHalls/halls.html', {"form": form})



def form_view(request,user_id):
        if request.method=="POST":
                form=CinemaHallForm(request.POST)

                k=0

                for place in Place.objects.all():
                    if place.place_name==form['cinemahall_place'].value():
                        k=1
                        obj=place
                        break
                if k==0:
                    obj = Place(place_name=form['cinemahall_place'].value())
                    obj.save()


                User=serviceprovider.objects.get(user_id=user_id)
                cinemaObj=CinemaHall(theatre_owner=User,current_movie=form['current_movie'].value(),cinemahall_name=form['cinemahall_name'].value(),seats=form['seats'].value(),timing=form['timing'].value(),cinemahall_address=form['cinemahall_address'].value(),cinemahall_place=obj,cinemahall_contactinfo=form['cinemahall_contactinfo'].value())
                cinemaObj.save()
                return render(request, "authentication/Serviceuserhomepage.html")


        else:
                form = CinemaHallForm()
                return  render(request,'CinemaHalls/halls.html', {"form": form})


def cinemahalls(request):

    return render(request,"CinemaHalls/cinemahalls.html",{
    'Place':Place.objects.all()
    })


def select(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    cinemahalls_info= CinemaHall.objects.filter(cinemahall_place=iid)
    context={'cinemahallsinfo': cinemahalls_info, }
    return render(request,"CinemaHalls/cinemahalls.html",{
    'Place':Place.objects.all(),
    'CinemaHalls':cinemahalls_info

    })



def CinemaHallListview(request,place_id):
    # model=Hotel
    # template_name='hotels/hotel_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
    
    place=Place.objects.get(id=place_id)
    theatre_list=CinemaHall.objects.filter(cinemahall_place=place)
    h = CinemaHallFilter(request.GET,queryset=theatre_list)

    return render(request,'cinemahalls/cinemahalls_list.html',{'filter': h,'cinemahall': theatre_list})




def aboutus(request):
    return render(request,"CinemaHalls/AboutUs.html")



