import django_filters
from .models import CinemaHall

class CinemaHallFilter(django_filters.FilterSet):

    class Meta:
        model=CinemaHall
        fields=('cinemahall_name','current_movie')