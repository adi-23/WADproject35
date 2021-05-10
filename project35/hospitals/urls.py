from django.urls import path
from . import views
from .views import HospitalDetailView,HospitalUpdateView

urlpatterns=[
   
    path('hospital/<int:pk>/',HospitalDetailView.as_view(),name="hospital_detail"),
    path('hospital/<int:pk>/update/',HospitalUpdateView.as_view(),name="hospital_update"),
    path('hospital/<int:user_id>/new',views.form_view,name="hospitals_form"),
    path('',views.hospitals,name="hospitals"),
    path('search/',views.search,name="hospitalsearch"),
    path('hospitalfilter/<int:place_id>',views.HospitalListview,name="hospitalfilterview"),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('home',views.homepage,name='homepage'),
]