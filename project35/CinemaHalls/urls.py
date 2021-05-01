from django.urls import path
from . import views


urlpatterns=[
#    path(r'^$',views.index,name='index'),
path('formpage/<int:user_id>',views.form_view,name='form'),
path('cinemahalls',views.cinemahalls,name='cinemahalls'),
 path('select/',views.select,name="select"),
  path('aboutus/',views.aboutus,name='aboutus'),
# path(r'admin/', admin.site.urls)
]
    


