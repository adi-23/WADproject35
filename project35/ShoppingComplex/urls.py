from django.urls import path
from . import views


urlpatterns=[
   
    path('form/<int:user_id>',views.form_view,name="shoppingcomplexform"),
    path('shoppingcomplex/',views.shoppingcomplex,name="shoppingcomplex"),
    path('search/',views.search,name="shoppingcomplexsearch"),
]