from django.urls import path
from . import views


urlpatterns=[
    path('',views.hotels,name="hotels"),
    path('hotel/',views.index,name="index"),
    path('add/<int:user_id>',views.add,name="add"),
    path('hotelfilter/<int:place_id>',views.HotelListview,name="HotelListview"),
    path('aboutus/',views.aboutus,name='aboutus'),
path('contact/',views.contact,name='contact'),
path('home',views.homepage,name='homepage'),
]
