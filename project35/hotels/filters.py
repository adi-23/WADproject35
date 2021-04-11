import django_filters
from .models import Hotel,Place

class HotelFilter(django_filters.FilterSet):
    

    class Meta:
        model=Hotel
        fields = ('hotel_place','hotel_hasACrooms')