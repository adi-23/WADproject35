from django.urls import path
from . import views

urlpatterns = [
    path('',views.shops,name='shops'),
    path('addshop',views.addshop,name="addshop")
]