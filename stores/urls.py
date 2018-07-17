from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('stores_list', views.stores_list, name='stores_list'),
    path('<int:store_id>/store_details/', views.store_details, name='store_details'),
    path('index_stores', views.index_stores, name='index_products'),
    path('<int:store_id>/details_store', views.details_store, name='details_store'),
    path('<int:store_id>/edit_store', views.edit_store, name='edit_store'),
    path('<int:store_id>/delete_store', views.delete_product, name='delete_store')
]
