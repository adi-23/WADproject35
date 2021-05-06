from django.urls import path
from . import views

urlpatterns = [
     path('<int:place_id>',views.shops,name='shopsfilter'),
     
    path('addshop/<int:user_id>',views.addshop,name="addshop"),
    path('editshop/<int:user_id>',views.editshops,name="editshops")
]