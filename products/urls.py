from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/product', views.product, name='products_details'),
    path('add_products/', views.pro, name='add_products'),
    path('', views.index_products, name='index_products')

]
