from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='login_page'),
   
]