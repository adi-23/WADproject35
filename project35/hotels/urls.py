from django.urls import path
from . import views
from .views import HotelDetailView,HotelUpdateView


urlpatterns=[

    path('hotel/<int:pk>/',HotelDetailView.as_view(),name="hotel_detail"),
    path('hotel/<int:pk>/update/',HotelUpdateView.as_view(),name="hotel_update"),
    path('',views.hotels,name="hotels"),
    path('hotel/',views.index,name="index"),
    path('hotel/<int:user_id>/new',views.add,name="hotel_form"),
    path('hotelfilter/<int:place_id>',views.HotelListview,name="HotelListview"),
    path('aboutus/',views.aboutus,name='aboutus'),
path('contact/',views.contact,name='contact'),
path('home',views.homepage,name='homepage'),
]
