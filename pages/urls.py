from django.contrib import admin

from django.urls import path

from . import views




urlpatterns = [
    path('', views.index,name="pages_index"),
    path('index', views.index),
    path('contact', views.contact),
    path('about', views.about,name="about"),
]