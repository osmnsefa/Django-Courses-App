from django.contrib import admin

from django.urls import path

from . import views




urlpatterns = [
    path('list', views.courses),
    path('<kurs_adi>', views.details),# dinamik url yapısı kullandık.Dinamik url'de her zaman üstten kontrole başlar.
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),# int olanı üste yadık çünkü bir sayıyı str olarak düşünüp name'i çalıştırabilir.
    path('kategori/<str:category_name>', views.getCoursesByCategory,name='courses_by_category'),
    
    
]