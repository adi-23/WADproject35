from django.urls import path,include
from . import views


urlpatterns = [
    #path('', views.home,name="home"),
    path('serviceuser_register/',views.serviceuser_register.as_view(),name="serviceuser_register"),
    path('serviceprovider_register/',views.serviceprovider_register.as_view(),name="serviceprovider_register"),
    path('login/',views.login_request,name="login"),
    path('logout/',views.logout_view,name="logout"),

]
