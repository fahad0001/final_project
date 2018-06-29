from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('stores_list', views.stores_list, name='stores_list'),
    path('<int:store_id>/store_details/', views.store_details, name='store_details')]
