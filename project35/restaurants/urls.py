from django.urls import path
from . import views

urlpatterns=[
     path('addrestaurent/<int:user_id>',views.restaurant_form,name="restaurant_form"),
     path('aboutus/',views.aboutus,name='aboutus'),
path('contact/',views.contact,name='contact'),
path('home',views.homepage,name='homepage'),
]