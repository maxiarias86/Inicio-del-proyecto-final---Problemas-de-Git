from django.shortcuts import render
from AppUsuarios.models import Usuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppUsuarios.forms import *
from django.contrib.auth.decorators import login_required

def inicioUsuarios(request):
    return render (request, 'AppUsuarios/inicioUsuarios.html')

@login_required
def crearMensaje(request):
    pass

@login_required
def listarMensajes(request):
    pass

@login_required
def responder(request):
    pass

@login_required
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
            return render(request,'AppUsuarios/login.html', {'form':form, 'mensaje':"Usuario y/o Contraseña incorrecto."})
    
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

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.descripcion=info["descripcion"]
            usuario.webpage=info["webpage"]
            usuario.avatar=info["avatar"]
            usuario.save()
            return render(request, "AppUsuarios/inicioUsuarios.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppUsuarios/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppUsuarios/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})