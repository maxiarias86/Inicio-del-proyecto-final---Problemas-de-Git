from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    descripcion=forms.CharField(label="Ingrese una breve descripción acerca de usted")
    webpage=forms.URLField(label='Dirección Web')

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2","descripcion","webpage"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email=forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir nueva contraseña", widget=forms.PasswordInput)
    descripcion=forms.CharField(label="Modificar su descripción")
    webpage=forms.URLField(label='Modificar Dirección Web')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2","descripcion","webpage"]
        help_texts = {k:"" for k in fields}