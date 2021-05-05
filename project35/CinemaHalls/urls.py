from django.urls import path
from . import views


urlpatterns=[
#    path(r'^$',views.index,name='index'),
path('formpage/<int:user_id>',views.form_view,name='form'),
path('cinemahalls',views.cinemahalls,name='cinemahalls'),
path('cinemahallsfilter/<int:place_id>',views.CinemaHallListview,name="cinemahallfilter"),
path('select/',views.select,name="select"),
path('aboutus/',views.aboutus,name='aboutus'),
path('contact/',views.contact,name='contact'),
path('home',views.homepage,name='homepage'),

]
    


