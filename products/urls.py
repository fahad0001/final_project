from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='products_details'),
    path('add_products', views.pro, name='add_products'),

]
