from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.drink_list, name="drink_list")
]      
