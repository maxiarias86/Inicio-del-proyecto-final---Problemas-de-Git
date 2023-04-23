from django.shortcuts import render
from AppUsuarios.models import Usuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppUsuarios.forms import *

# Create your views here.
def inicioUsuarios(request):
    return render (request, 'AppUsuarios/inicioUsuarios.html')

def crearMensaje(request):
    pass

def listarMensajes(request):
    pass

def responder(request):
    pass

def leerMensaje(request):
    pass

def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario=info['username']
            contra=info['password']

            user=authenticate(username=usuario,password=contra)

            if user is not None:
                login(request, user)
                return render(request,'AppUsuarios/inicioUsuarios.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request,'AppUsuarios/login.html', {'form':form, 'mensaje':"Usuario y/o Contraseña incorrectos"})
        else:
            return render(request,'AppUsuarios/login.html', {'form':form, 'mensaje':"Error en el formulario"})
    
    form= AuthenticationForm()

    return render (request, 'AppUsuarios/login.html', {'form':form})

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, 'AppUsuarios/inicioUsuarios.html', {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppUsuarios/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppUsuarios/register.html", {"form": form})