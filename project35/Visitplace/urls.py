from django.urls import path
from . import views

urlpatterns= [
   path('attraction/',views.show,name='show'),
   path('visitplace/',views.select1,name='select1'),
   path('',views.visitplaces,name='visitplaces'),
   path('aboutus/',views.aboutus,name='aboutus'),
path('contact/',views.contact,name='contact'),
path('home',views.homepage,name='homepage'),

]