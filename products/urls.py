from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:product_id>/product', views.product, name='products_details'),
    path('add_products/', views.pro, name='add_products'),
    path('', views.index_products, name='index_products'),
    path('<int:product_id>/detail_product', views.detail_product, name='detail_product'),
    path('<int:product_id>/edit_product', views.edit_product, name='edit_product'),
    path('<int:product_id>/delete_product', views.delete_product, name='delete_product')
]


