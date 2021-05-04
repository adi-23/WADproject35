from django.urls import path
from . import views

urlpatterns=[
     path('addrestaurent/<int:user_id>',views.restaurant_form,name="restaurant_form"),
    
]