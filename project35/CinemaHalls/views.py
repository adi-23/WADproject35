from django.shortcuts import render
from hotels.models import Place
from .models import CinemaHall
from .form import CinemaHallForm
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

# def form_view(request):
    
#     form = CinemaHallForm()
#     return  render(request,'CinemaHalls/halls.html', {"form": form})



def form_view(request):
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



                cinemaObj=CinemaHall(cinemahall_name=form['cinemahall_name'].value(),seats=form['seats'].value(),timing=form['timing'].value(),cinemahall_address=form['cinemahall_address'].value(),cinemahall_place=obj,cinemahall_contactinfo=form['cinemahall_contactinfo'].value())
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



def aboutus(request):
    return render(request,"CinemaHalls/AboutUs.html")