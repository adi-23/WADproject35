import django_filters
from .models import Hotel,Place

class HotelFilter(django_filters.FilterSet):
    # hotel_place = django_filters.ModelMultipleChoiceFilter(queryset=Place.objects.all(),
    
    # label="Place",
    # label_suffix="")
    hotel_hasACrooms = django_filters.BooleanFilter()

    class Meta:
        model=Hotel
        fields = ('hotel_place','hotel_hasACrooms')