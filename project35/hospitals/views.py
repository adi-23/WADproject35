from django.shortcuts import render
from .form import HospitalForm
from hotels.models import Place
from .models import Hospital


# Create your views here.

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





def form_view(request):
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

        hospital = Hospital(doctors=form['doctors'].value(),hospital_name=form['hospitalName'].value(),hospital_image=form['hospitalImage'].value(),hospital_place=obj,hospital_address=form['hospitalAddress'].value(),hospital_contactinfo=form['hospitalContactinfo'].value())
        hospital.save()
        return render(request,'authentication/Serviceuserhomepage.html')
    else:
        form= HospitalForm()
        return render(request,'hospitals/form.html',{'form':form})


def hospitals(request):
    places=Place.objects.all()
    return render(request,'hospitals/hospitals.html',{'Place':places})
