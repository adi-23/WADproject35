from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('login',views.login,name="login"),
    path('register',views.registerView,name="register"),
    path('forget',views.forget,name="forget"),
    path('logout',views.logout,name="logout"),
]

