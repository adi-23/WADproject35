from django.urls import path
from . import views


urlpatterns=[
   
    path('form/',views.form_view,name="hospitalsform"),
    path('hospitals/',views.hospitals,name="hospitals"),
    path('search/',views.search,name="hospitalsearch"),
]