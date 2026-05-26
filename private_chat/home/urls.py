
# from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    
    path('', views.load, name='load'),
    path('login/', views.login, name='login'), 
    path('main/', views.main, name='main'),
]
