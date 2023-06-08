from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    
    path("home/", views.home ,name="home"),
    path("", views.home ,name="home"),
    path("std/", views.std_add ,name="std"),
    path("del/<int:roll>", views.delete_std, name="del"),
    path("update/<int:roll>", views.update_std, name="update"),
    path("edit/<str:id>", views.edit, name="edit" ),
]
