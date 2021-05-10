import django_filters
from .models import ShoppingComplex

class ShoppingComplexFilter(django_filters.FilterSet):

    class Meta:
        model=ShoppingComplex
        fields=('shoppingcomplex_name','shoppingcomplex_hasFloors')