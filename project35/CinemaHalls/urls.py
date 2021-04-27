from django.urls import path
from . import views


urlpatterns=[
#    path(r'^$',views.index,name='index'),
path('formpage/',views.form_view,name='form'),
path('',views.cinemahalls,name='cinemahalls'),
 path('cinemahalls/',views.select,name="select"),
  path('aboutus/',views.aboutus,name='aboutus'),
# path(r'admin/', admin.site.urls)
]
    


