from django.urls import path
from . import views

urlpatterns = [
    #path('',views.shop,name='shop'),
    path('addshop',views.addshop,name="addshop")
]