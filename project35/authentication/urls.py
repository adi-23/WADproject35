from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home,name="home"),
    path('serviceuser_register/',views.serviceuser_register.as_view(),name="serviceuser_register"),#url for registration of serviceuser
    path('serviceprovider_register/',views.serviceprovider_register.as_view(),name="serviceprovider_register"),#url for registration of serviceprovider
    path('login/',views.login_request,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('serviceproviderhome/',views.serviceproviderhome,name="serviceproviderhome"),
    path('userhome/',views.userhome,name="userhome"),


]
