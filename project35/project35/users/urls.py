from django.contrib import admin
from django.urls import path,include
import django.contrib.auth.urls
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('home/',views.home,name="home"),    
   # path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('users/',include('django.contri.auth.urls')),
    
]
