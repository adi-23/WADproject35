from django.shortcuts import render
from .models import Place,Hotel
# Create your views here.
# def hotels(request):
#     placeid = Place.objects.filter(place_name='palakollu')
#     hotels_info= Hotel.objects.filter(hotel_place = placeid.get(id=2))
#     context={'hotelsinfo': hotels_info, }
#     return render(request,"hotels/base.html",context)
def hotels(request):
    iid=0
    for place in Place.objects.all():
        if place.place_name=='guntur':
            iid=place.id
            break

    hotels_info= Hotel.objects.filter(hotel_place=iid)
    context={'hotelsinfo': hotels_info, }
    return render(request,"hotels/base.html",context)

