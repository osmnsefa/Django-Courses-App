from django.contrib import admin

from django.urls import path

from . import views




urlpatterns = [
    path('', views.index,name="index"),  #alttaki kodda slug veri tipinde slug adında bir değişken belirledik.
    path('search', views.search, name="search"),
    path('create-course', views.create_course, name="create-course"),
    path('course-list',views.course_list,name="course_list"),
    path('course-edit/<int:id>',views.course_edit,name="course_edit"),
    path('upload',views.upload,name="upload_image"),
    path('course-delete/<int:id>',views.course_delete,name="course_delete"),
    path('<slug:slug>', views.details,name="course_details"),# dinamik url yapısı kullandık.Dinamik url'de her zaman üstten kontrole başlar.
    path('kategori/<slug:slug>', views.getCoursesByCategory,name='courses_by_category'),
    
    
]