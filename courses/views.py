from datetime import date,datetime
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Slider, UploadModel, course,Categories  #verileri aldığımız obje
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.


def index(request):
    # list comphension
    kurslar=course.objects.filter(isActive=1,isHome=1)
    kategoriler=Categories.objects.all()
    sliders=Slider.objects.filter(is_active=True)
    
    return render(request,"courses/index.html",{
        'categories':kategoriler,
        'courses':kurslar,
        'sliders':sliders
    })
    
def isAdmin(user):
    return user.is_superuser

    
@user_passes_test(isAdmin)    #Superuser olup olmadığını kontrol ettik.
def create_course(request):
    if request.method== "POST":
        form=CourseCreateForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("/kurslar")    
    else:    
        form = CourseCreateForm()
    return render(request,"courses/create-course.html",{"form":form})
@user_passes_test(isAdmin)
def course_list(request):
    kurslar=course.objects.all()
    return render(request,"courses/course-list.html",{
        'courses':kurslar
    })    
@login_required()    
def course_edit(request,id):
    kurs=get_object_or_404(course,pk=id)
    
    if request.method=="POST":
        form=CourseEditForm(request.POST,request.FILES,instance=kurs)#kullanıcının girdiği bilgiler ile formdakiler karşılaştırılır,sadece değiştirilen bilgiler güncellenir.
        form.save()
        return redirect("course_list")
    else:
        form=CourseEditForm(instance=kurs)
    
    return render(request,"courses/edit-course.html",{"form":form})
@login_required()
def course_delete(request,id):
    kurs=get_object_or_404(course,pk=id)
    if request.method == "POST":
        kurs.delete()
        return redirect("course_list")
    return render(request,"courses/course-delete.html",{"course":kurs})
@login_required()
def upload(request):
    if request.method == "POST":
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            model=UploadModel(image=request.FILES["image"])
            model.save()
            return render(request,"courses/success.html")
    else:    
        form=UploadForm()
    return render(request,"courses/upload.html",{"form":form})

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q= request.GET["q"]
        kurslar=course.objects.filter(isActive=True,title__contains=q).order_by('date')
        kategoriler=Categories.objects.all()
    else:
        return redirect("/kurslar")
    
    
    return render(request,"courses/search.html",{
        'categories':kategoriler,
        'courses':kurslar,
        
    })

def details(request,slug):
    #try:
      #  kurs=course.objects.get(slug=slug)
    #except:
     #   raise Http404()
    kurs=get_object_or_404(course, slug=slug) # başta id'ye göre yapmıştık slug olarak değiştirdik.
    
    context={
        'course' : kurs
    }
    
    return render(request,"courses/details.html",context)
def getCoursesByCategory(request,slug):
    kurslar=course.objects.filter(Categories__slug=slug,isActive=True).order_by('date')
    kategoriler=Categories.objects.all()
    
    paginator=Paginator(kurslar,2)
    page=request.GET.get('page',1)
    page_obj=paginator.page(page)
    
    return render(request,"courses/list.html",{
        'categories':kategoriler,
        'page_obj':page_obj,
        'seciliKategori':slug
    })

