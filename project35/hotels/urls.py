from django.urls import path
from . import views


urlpatterns=[
    path('',views.hotels,name="hotels"),
    path('hotel/',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('hotelfilter/<int:place_id>',views.HotelListview,name="HotelListview")

]
