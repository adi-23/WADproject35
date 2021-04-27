from django.urls import path
from . import views

urlpatterns= [
   path('attraction/',views.show,name='show'),
   path('visitplace/',views.select1,name='select1'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path('',views.visitplaces,name='visitplaces'),
]