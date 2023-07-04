from django.contrib import admin

from django.urls import path

from . import views




urlpatterns = [
    path('', views.home),
    path('anasayfa', views.home),
    path('contact', views.contact),
    path('about', views.about),
]