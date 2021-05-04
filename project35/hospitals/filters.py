import django_filters
from .models import Hospital

class HospitalFilter(django_filters.FilterSet):
    class Meta:
        model=Hospital
        fields=('hospital_name','doctors')
