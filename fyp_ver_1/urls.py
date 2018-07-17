from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/register/', views.signup, name='register'),
    path('home', views.home, name='home'),
    path('login', LoginView.as_view(template_name="Index/signin.html"), name="user_login"),
    path('logout', LogoutView.as_view(), name="user_logout"),
    path('home/contact_us', views.contact_us, name='contact_us'),
    path('contact',views.view_contacts,name='contact')
]