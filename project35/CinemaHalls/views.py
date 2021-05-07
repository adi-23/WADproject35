from django.shortcuts import render,redirect
from hotels.models import Place
from .models import CinemaHall
from .form import CinemaHallForm
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from authentication.models import serviceprovider,User
from .filters import CinemaHallFilter
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)




def form_view(request,user_id):
    
    if request.method == "POST":
        form=CinemaHallForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places:
            if form['cinemahall_place'].value() == place.place_name:
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['cinemahall_place'].value())
            obj.save()
        user=User.objects.get(id=user_id)
        cinemaObj=CinemaHall(theatre_owner=user,current_movie=form['current_movie'].value(),cinemahall_name=form['cinemahall_name'].value(),seats=form['seats'].value(),timing=form['timing'].value(),cinemahall_address=form['cinemahall_address'].value(),cinemahall_place=obj,cinemahall_contactinfo=form['cinemahall_contactinfo'].value(),cinemahall_image=form['cinemahall_image'].value())
        cinemaObj.save()
                
        return render(request,'authentication/Serviceuserhomepage.html')
    else:
        if (CinemaHall.objects.filter(theatre_owner_id=user_id).first()) is not None:
            temp =CinemaHall.objects.filter(theatre_owner_id=user_id).first()
            i=temp.id
            url = '/cinemahalls/cinemahall/{}/'.format(i)
            return redirect(url)

        else:
            form= CinemaHallForm()
            return render(request,'CinemaHalls/cinemahall_form.html',{'form':form})

class CinemaHallDetailView(DetailView):
    model=CinemaHall


class CinemaHallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=CinemaHall
    fields=['cinemahall_name','cinemahall_image','seats','cinemahall_address','cinemahall_place','cinemahall_contactinfo','timing','current_movie']

    def form_valid(self, form):
        if self.request.user.is_serviceprovider :
            form.instance.theatre_owner = self.request.user
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the Cinemahalls')

    def test_func(self):
        cinemahall =self.get_object()
        if self.request.user == cinemahall.theatre_owner:
            return True
        return False


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
    'Place': Place.objects.all(),
    'CinemaHalls':cinemahalls_info,
    'place_id': iid

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
    return render(request,"Visitplace/AboutUs.html")


def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')