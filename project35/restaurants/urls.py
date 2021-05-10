from django.urls import path
from . import views
from .views import RestaurantDetailView,RestaurantUpdateView

urlpatterns=[
    
     path('aboutus/',views.aboutus,name='aboutus'),
     path('contact/',views.contact,name='contact'),
     path('home',views.homepage,name='homepage'),
     path('restaurantfilter/<int:place_id>',views.RestaurantListview,name="restaurantfilter"),
     path('restaurant/',views.restaurant,name="restaurant"),
     path('search/',views.search,name="restsearch"),
     path('restaurant/<int:pk>/',RestaurantDetailView.as_view(),name="restaurant_detail"),
    path('restaurant/<int:pk>/update/',RestaurantUpdateView.as_view(),name="restaurant_update"),
    path('restaurant/<int:user_id>/new',views.resta_view,name="restaurant_form"),
]