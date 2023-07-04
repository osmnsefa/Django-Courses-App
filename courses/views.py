from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

data={
    "programlama":"Programlama kategorisi",
    "web-gelistirme":"Web geliştirme kategorisi",
    "mobil":"Mobil kategorisi"
    
}

def courses(request):
    return HttpResponse("Kurs Listesi")
def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")
def getCoursesByCategory(request,category_name):
    try:
        category_text=data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")
def getCoursesByCategoryId(request,category_id):
    category_list=list(data.keys())
    if(category_id> len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category_name= category_list[category_id-1]
    
    redirect_url=reverse('courses_by_category',args=[category_name])
    
    return redirect(redirect_url)
