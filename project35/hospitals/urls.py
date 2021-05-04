from django.urls import path
from . import views


urlpatterns=[
   
    path('form/<int:user_id>',views.form_view,name="hospitalsform"),
    path('hospitals/',views.hospitals,name="hospitals"),
    path('search/',views.search,name="hospitalsearch"),
    path('hospitalfilter/<int:place_id>',views.HospitalListview,name="hospitalfilterview")
]