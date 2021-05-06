from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import HospitalForm
from hotels.models import Place
from .models import Hospital
from authentication.models import serviceprovider,User
from .filters import HospitalFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)

# Create your views here.

class HospitalDetailView(DetailView):
    model=Hospital


class HospitalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Hospital
    fields=['hospital_name','hospital_image','doctors','hospital_address','hospital_place','hospital_contactinfo']

    def form_valid(self, form):
        if self.request.user.is_serviceprovider :
            form.instance.hospital_sp = self.request.user
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the hospitals')

    def test_func(self):
        hospital =self.get_object()
        if self.request.user == hospital.hospital_sp:
            return True
        return False




def search(request):
    result=request.GET['places']
    iid=0
    for place in Place.objects.all():
        if place.place_name==result:

            iid=place.id
            break

    hospitals_info= Hospital.objects.filter(hospital_place_id=iid)
    p = Place.objects.filter(id=iid)
    context={'hospitalsinfo': hospitals_info, }
    return render(request,"hospitals/hospitals.html",{
    'Place':Place.objects.all(),
    'Hospitals':hospitals_info,'place':p

    })





def form_view(request,user_id):
    if request.method == "POST":
        form=HospitalForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places:
            if form['hospitalPlace'].value() == place.place_name:
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['hospitalPlace'].value())
            obj.save()
        h_sp=User.objects.get(id=user_id)
        hospital = Hospital(hospital_sp=h_sp,doctors=form['doctors'].value(),hospital_name=form['hospitalName'].value(),hospital_image=form['hospitalImage'].value(),hospital_place=obj,hospital_address=form['hospitalAddress'].value(),hospital_contactinfo=form['hospitalContactinfo'].value())
        hospital.save()
        return render(request,'authentication/Serviceuserhomepage.html')
    else:
        if (Hospital.objects.filter(hospital_sp_id=user_id).first()) is not None:
            temp = Hospital.objects.filter(hospital_sp_id=user_id).first()
            i=temp.id
            url = '/hospitals/hospital/{}/'.format(i)
            return redirect(url)
        
        else:
            form= HospitalForm()
            return render(request,'hospitals/hospital_form.html',{'form':form})


def hospitals(request):
    places=Place.objects.all()
    return render(request,'hospitals/hospitals.html',{'Place':places})



def HospitalListview(request,place_id):
    # model=Hotel
    # template_name='hotels/hotel_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
    
    place=Place.objects.get(id=place_id)
    hospital_list=Hospital.objects.filter(hospital_place=place)
    h = HospitalFilter(request.GET,queryset=hospital_list)

    return render(request,'hospitals/hospital_list.html',{'filter': h,'hospital': hospital_list})


def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")


def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')
