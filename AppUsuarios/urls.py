from django.urls import path
from AppUsuarios.views import *

urlpatterns = [
    
    path("", inicioUsuarios, name="inicioUsuarios"),
    path('login/', login_request,name="login"),
    path('register/', register, name='register'),
        
]