from django.urls import path
from AppUsuarios.views import *

urlpatterns = [
    
    path("", inicioUsuarios, name="inicioUsuarios"),
        
]