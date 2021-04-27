from django.shortcuts import render
from hotels.models import Place
from .models import Attractions
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse


# Create your views here.

def show(request):
    return render(request,'Visitplace/attractions.html',{'Place':Place.objects.all()})


def select1(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    visitplaces_info= Attractions.objects.filter(attraction_place=iid)
    context={'visitplacesinfo': visitplaces_info, }
    return render(request,"Visitplace/attractions.html",{
    'Place':Place.objects.all(),
    'Visitplace':visitplaces_info

    })


def visitplaces(request):

    return render(request,"Visitplace/attractions.html",{
    'Place':Place.objects.all()
    })

def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")
