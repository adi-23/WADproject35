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
from django.views.generic import ( # Used class based generic views for details and updating the information
    DetailView,
    UpdateView,
)




def form_view(request,user_id):
    
    if request.method == "POST": #If method is POST the data sent through form
        form=CinemaHallForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places: # If the serviceprovider specified place is not in the database, Add it to the table 
            if form['cinemahall_place'].value() == place.place_name:
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['cinemahall_place'].value())
            obj.save()
        # Storing and saving the cinema hall details in the database
        user=User.objects.get(id=user_id) # Searching the user information based on user id
        cinemaObj=CinemaHall(theatre_owner=user,current_movie=form['current_movie'].value(),cinemahall_name=form['cinemahall_name'].value(),seats=form['seats'].value(),timing=form['timing'].value(),cinemahall_address=form['cinemahall_address'].value(),cinemahall_place=obj,cinemahall_contactinfo=form['cinemahall_contactinfo'].value(),cinemahall_image=form['cinemahall_image'].value())
        cinemaObj.save()
                
        return render(request,'authentication/Serviceuserhomepage.html')
    else: # If the serviceprovider has already added cinema hall details then get the detailed information of their cinema hall otherwise render the cinema hall form 
        if (CinemaHall.objects.filter(theatre_owner_id=user_id).first()) is not None:
            temp =CinemaHall.objects.filter(theatre_owner_id=user_id).first() # Looking for information of their cinema hall
            i=temp.id
            url = '/cinemahalls/cinemahall/{}/'.format(i)
            return redirect(url)

        else:
            form= CinemaHallForm()
            return render(request,'CinemaHalls/cinemahall_form.html',{'form':form})

class CinemaHallDetailView(DetailView): # With the help of DetailView, we can get detailed information of each cinema hall
    model=CinemaHall


class CinemaHallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Using UpdateView, we are updating the cinema hall details
    model=CinemaHall
    fields=['cinemahall_name','cinemahall_image','seats','cinemahall_address','cinemahall_place','cinemahall_contactinfo','timing','current_movie']

    def form_valid(self, form): # Here, if a person is serviceprovider then he/she can edit the form instance
        if self.request.user.is_serviceprovider :
            form.instance.theatre_owner = self.request.user # Storing the user details in the form
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the Cinemahalls') # Only serviceprovider can edit the form, users can't edit it.

    def test_func(self):
        cinemahall =self.get_object()
        if self.request.user == cinemahall.theatre_owner: # Checking whether the current login user is the owner of the cinema hall
            return True
        return False


def cinemahalls(request):

    return render(request,"CinemaHalls/cinemahalls.html",{
    'Place':Place.objects.all()
    })

# Searching respective cinemahalls details in a specified location
def select(request):
    result=request.GET['places'] # specified location
    iid=0
    for place in Place.objects.all(): # Searching the id of specified location in the database
        if place.place_name==result:

            iid=place.id
            break

    cinemahalls_info= CinemaHall.objects.filter(cinemahall_place=iid) # Filtering the cinemahalls according to the place
    context={'cinemahallsinfo': cinemahalls_info, }
    return render(request,"CinemaHalls/cinemahalls.html",{ # Rendering the cinema hall details in the user specified location
    'Place': Place.objects.all(),
    'CinemaHalls':cinemahalls_info,
    'place_id': iid

    })


# Filtering and getting the cinema hall names based on doctors information
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



# About our Website
def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")

# Information about website owners
def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')