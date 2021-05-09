from django.urls import path
from . import views
from .views import (
    ShoppingComplexDetailView,
    ShoppingComplexUpdateView,
)


urlpatterns=[
   
    path('shoppingcomplex/<int:user_id>/new',views.form_view,name="shoppingcomplex_form"),
    path('shoppingcomplex/',views.shoppingcomplex,name="shoppingcomplex"),
    path('search/',views.search,name="shoppingcomplexsearch"),
    path('shoppingcomplexfilter/<int:place_id>',views.ShoppingComplexListview,name="shoppingcomplexfilter"),
    path('shoppingcomplex/<int:pk>/',ShoppingComplexDetailView.as_view(),name="shoppingcomplex_detail"),
    path('shoppingcomplex/<int:pk>/update/',ShoppingComplexUpdateView.as_view(),name="shoppingcomplex_update"),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('home',views.homepage,name='homepage'),

]