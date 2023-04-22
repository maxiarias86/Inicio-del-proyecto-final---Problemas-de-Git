from django.db import models

# Create your models here.

class Usuario(models.Model):
    #avatar=models.ImageField()
    username=models.CharField(max_length=30,unique=True)
    descripcion=models.CharField(max_length=20000)
    pagina=models.URLField()
    mail=models.EmailField(unique=True)
    password=models.CharField(max_length=15)

'''
class Mensaje(models.Model):
    remitente=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    destinatario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido=models.CharField(max_length=1000)
'''