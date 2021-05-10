import django_filters
from .models import Restaurant

class RestaurantFilter(django_filters.FilterSet):

    class Meta:
        model=Restaurant
        fields=('resta_name','restaurant_type','has_delivery','has_AC','has_parking')

