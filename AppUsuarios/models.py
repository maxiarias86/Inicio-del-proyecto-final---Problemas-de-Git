from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    usuario=models.CharField(max_length=30,unique=True)
    descripcion=models.CharField(max_length=20000)
    pagina=models.URLField()
    mail=models.EmailField(unique=True)
    contra=models.CharField(max_length=15)

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Mensaje(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    destinatario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=1000)
    fecha=models.DateField()