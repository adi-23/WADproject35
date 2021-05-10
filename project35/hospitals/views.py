from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import HospitalForm
from hotels.models import Place
from .models import Hospital
from authentication.models import serviceprovider,User
from .filters import HospitalFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( # Used class based generic views for details and updating the information
    DetailView,
    UpdateView,
)

# Create your views here.

class HospitalDetailView(DetailView): # With the help of DetailView, we can get detailed information of each hospital 
    model=Hospital


class HospitalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Using UpdateView, we are updating the hospital details
    model=Hospital
    fields=['hospital_name','hospital_image','doctors','hospital_address','hospital_place','hospital_contactinfo']

    def form_valid(self, form): # Here, if a person is serviceprovider then he/she can edit the form instance
        if self.request.user.is_serviceprovider :
            form.instance.hospital_sp = self.request.user # Storing the user details in the form
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the hospitals') # Only serviceprovider can edit the form, users can't edit it.

    def test_func(self):
        hospital =self.get_object()
        if self.request.user == hospital.hospital_sp: # Checking whether the current login user is the owner of the hospital
            return True
        return False



# Searching respective hospitals details in a specified location
def search(request):
    result=request.GET['places'] # specified location
    iid=0
    for place in Place.objects.all(): # Searching the id of specified location in the database
        if place.place_name==result:

            iid=place.id
            break

    hospitals_info= Hospital.objects.filter(hospital_place_id=iid) # Filtering the hospitals according to the place
    p = Place.objects.filter(id=iid)
    context={'hospitalsinfo': hospitals_info, }
    return render(request,"hospitals/hospitals.html",{ # Rendering the hospital details in the user specified location
    'Place':Place.objects.all(),
    'Hospitals':hospitals_info,'place':p,
    'place_id':iid

    })





def form_view(request,user_id):
    if request.method == "POST": #If method is POST the data sent through form
        form=HospitalForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places: # If the serviceprovider specified place is not in the database, Add it to the table 
            if form['hospitalPlace'].value() == place.place_name:
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['hospitalPlace'].value())
            obj.save()
        # Storing and saving the hospital details in the database
        h_sp=User.objects.get(id=user_id) # Searching the user information based on user id
        hospital = Hospital(hospital_sp=h_sp,doctors=form['doctors'].value(),hospital_name=form['hospitalName'].value(),hospital_image=form['hospitalImage'].value(),hospital_place=obj,hospital_address=form['hospitalAddress'].value(),hospital_contactinfo=form['hospitalContactinfo'].value())
        hospital.save()
        return render(request,'hotels/redir.html')
    else: # If the serviceprovider has already added hospital details then get the detailed information of their hospital otherwise render the hospital form 
        if (Hospital.objects.filter(hospital_sp_id=user_id).first()) is not None:
            temp = Hospital.objects.filter(hospital_sp_id=user_id).first() # Looking for information of their hospital
            i=temp.id
            url = '/hospitals/hospital/{}/'.format(i)
            return redirect(url)
        
        else:
            form= HospitalForm()
            return render(request,'hospitals/hospital_form.html',{'form':form})


def hospitals(request):
    places=Place.objects.all()
    return render(request,'hospitals/hospitals.html',{'Place':places})


# Filtering and getting the hospital names based on doctors information
def HospitalListview(request,place_id):
    
    place=Place.objects.get(id=place_id)
    hospital_list=Hospital.objects.filter(hospital_place=place)
    h = HospitalFilter(request.GET,queryset=hospital_list)

    return render(request,'hospitals/hospital_list.html',{'filter': h,'hospital': hospital_list,'place':place})

# About our Website
def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")

# Information about website owners
def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')
