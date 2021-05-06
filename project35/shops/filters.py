import django_filters
from .models import Shop

class ShopFilter(django_filters.FilterSet):

    class Meta:
        model=Shop
        fields=('shop_name','shop_itemtype')