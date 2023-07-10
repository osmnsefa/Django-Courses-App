from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.forms import widgets
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    def __init__(self,  *args, **kwargs) :
        super().__init__( *args,**kwargs)
        self.fields["username"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget=widgets.PasswordInput(attrs={"class":"form-control"})



class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","first_name","last_name",)
    def __init__(self,  *args, **kwargs) :
        super().__init__( *args,**kwargs)
        self.fields["username"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["email"].widget=widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["first_name"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].required=True
        
    def clean_email(self):
        email=self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            self.add_error("email","email daha önce kullanılmış") # email kısmına yeni fonksiyon ekledik.       
        return email
class UserPasswordChangeForm(PasswordChangeForm):
    
    def __init__(self,  *args, **kwargs) :
        super().__init__( *args,**kwargs)
        self.fields["new_password1"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["old_password"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
       
    
    
    
    
    