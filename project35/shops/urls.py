from django.urls import path
from . import views

urlpatterns = [
    path('',views.shops,name='shops'),
    path('addshop/<int:user_id>',views.addshop,name="addshop"),
    path('editshop/<int:user_id>',views.editshops,name="editshops")
]