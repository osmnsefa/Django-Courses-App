from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Categories(models.Model):
    name=models.CharField( max_length=50)
    slug=models.SlugField(default="",blank=True,null=False,unique=True,db_index=True)
    
    def __str__(self) :
        return f"{self.name}"

class course(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=100,default="")
    description=RichTextField()
    image=models.ImageField(upload_to="images",default="")
    date=models.DateField(auto_now=True)
    isActive=models.BooleanField(default=False)
    isHome=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=True,null=False,unique=True,db_index=True) # bu kolonu sonradan eklediğimiz ve verisi olmadığı için varsayılan olarak boş yaptık
    # aynı slugfield'lar olmasın diye unique ve db_index parametrelerini kullanıyoruz.
    Categories=models.ManyToManyField(Categories)
    
    def __str__(self) :
        return f"{self.title}" # admin panelinde modellerin üzerinde ismi ve tarihi yazar.
    
class Slider(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    is_active=models.BooleanField(default=False)
    course=models.ForeignKey(course,on_delete=models.SET_NULL,null=True,blank=True)   
    
    def __str__(self):
        return f"{self.title}"
class UploadModel(models.Model):
    image=models.ImageField(upload_to="images")    
    

