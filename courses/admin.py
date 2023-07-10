from django.contrib import admin
from .models import Slider, course,Categories
# Register your models here.
@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","slug","category_list")
    list_display_links =("title","slug")
    prepopulated_fields = {"slug":("title",),} #title'a göre slug belirler.
    list_filter=("title","isActive","isHome")
    list_editable=("isActive","isHome")
    search_fields=("title","description")
    
    def category_list(self,obj):
        html=""
        for category in obj.Categories.all():
            html += category.name + " "
        return html
    
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count")
    prepopulated_fields = {"slug":("name",),}
    
    def course_count(self,obj):
        return obj.course_set.count()
admin.site.register(Slider)    




