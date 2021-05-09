from django.urls import path
from . import views
from .views import (
    CinemaHallDetailView,
    CinemaHallUpdateView,
)



urlpatterns=[

path('cinemahalls',views.cinemahalls,name='cinemahalls'),
path('cinemahallsfilter/<int:place_id>',views.CinemaHallListview,name="cinemahallfilter"),
path('cinemahall/<int:user_id>/new/',views.form_view,name="cinemahall_form"),
path('cinemahall/<int:pk>/',CinemaHallDetailView.as_view(),name="cinemahall_detail"),
path('cinemahall/<int:pk>/update/',CinemaHallUpdateView.as_view(),name="cinemahall_update"),
path('select/',views.select,name="select"),
path('aboutus/',views.aboutus,name='aboutus'),
path('contact/',views.contact,name='contact'),
path('home',views.homepage,name='homepage'),

]
    


