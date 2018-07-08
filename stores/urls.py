from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('stores_list', views.stores_list, name='stores_list'),
    path('<int:store_id>/store_details/', views.store_details, name='store_details'),
    path('index_stores', views.index_stores, name='index_products'),
    path('details_store',views.details_store, name='details_store')
]
