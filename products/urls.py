from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list,name='products_list'),
    path('add_products', views.pro, name='add_products')
]
