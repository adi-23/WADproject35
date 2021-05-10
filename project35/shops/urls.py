from django.urls import path
from . import views
from .views import ShopDetailView,ShopUpdateView

urlpatterns = [
     path('<int:place_id>',views.shops,name='shopsfilter'),
     path('search/',views.search,name="shopsSearch"),
     path('shops/',views.shopcomplex,name="shopDet"),
     
    
    path('editshop/<int:user_id>',views.editshops,name="editshops"),
    path('shop/<int:pk>/',ShopDetailView.as_view(),name="shop_detail"),
    path('shop/<int:pk>/update/',ShopUpdateView.as_view(),name="shop_update"),
    path('shop/<int:user_id>/new',views.form_view,name="shop_form")

]