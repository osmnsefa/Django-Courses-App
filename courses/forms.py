
from django import forms
from django.forms import SelectMultiple,TextInput,Textarea
from courses.models import course 


# class CourseCreateForm(forms.Form):
#     title = forms.CharField(label="Kurs Başlığı",required=True,error_messages={"required":"kurs başlığı giriniz."},
#         widget=forms.TextInput(attrs={"class":"form-control"}))
#     description=forms.CharField(label="Açıklama",widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl=forms.CharField(label="Görsel",widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug=forms.SlugField(label="Slug",widget=forms.TextInput(attrs={"class":"form-control"}))


class CourseCreateForm(forms.ModelForm):   
    class Meta:
        model=course
        fields=("title","description","image","slug")
        labels={
            'title':'Kurs Başlığı',
            'description':"Açıklama"
        }
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"}),
        }
        error_messages={
            "title":{
                "required":"Kurs başlığı girmelisiniz...",
                "max_length":"maksimum 50 karakter girmelisiniz..."
            },
            "description":{
                "required":"Kurs açıklaması gereklidir..."
            }
        }
class CourseEditForm(forms.ModelForm):   
    class Meta:
        model=course
        fields=("title","description","image","slug","Categories","isActive")
        labels={
            'title':'Kurs Başlığı',
            'description':"Açıklama"
        }
        widgets={
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            "Categories":SelectMultiple(attrs={"class":"form-control"}),
        }
        error_messages={
            "title":{
                "required":"Kurs başlığı girmelisiniz...",
                "max_length":"maksimum 50 karakter girmelisiniz..."
            },
            "description":{
                "required":"Kurs açıklaması gereklidir..."
            }
        }
class UploadForm(forms.Form):
    image=forms.ImageField()    
    