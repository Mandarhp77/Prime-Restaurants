from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hotels/', views.home, name='home'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_data', views.get_data, name='get_data')
]