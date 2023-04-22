from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    descripcion=forms.CharField(label="Ingrese una breve descripción acerca de usted")
    webpage=forms.URLField(label='Dirección Web')
    avatar=forms.ImageField(label='Avatar')

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2","descripcion","webpage","avatar"]
        help_texts = {k:"" for k in fields}