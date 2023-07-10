from django.shortcuts import render
from django.http import HttpResponse

from courses.models import Slider

# Create your views here.

def index(request):
    sliders=Slider.objects.filter(is_active=True)
    
    return render(request,"pages/index.html",{
        
        'sliders':sliders
    })
def about(request):
    return render(request,"pages/about.html")
def contact(request):
    return render(request,"pages/contact.html")