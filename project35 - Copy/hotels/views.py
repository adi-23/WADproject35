from django.shortcuts import render
from .models import Place,Hotel
# Create your views here.
def hotels(request):
    placeid = Place.objects.filter(place_name='palakollu')
    hotels_info= Hotel.objects.filter(hotel_place = placeid.get(id=2))
    context={'hotelsinfo': hotels_info, }
    return render(request,"hotels/base.html",context)
