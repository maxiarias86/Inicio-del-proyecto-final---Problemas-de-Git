from django.urls import path
from AppUsuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicioUsuarios, name="inicioUsuarios"),
    path('login/', login_request,name="login"),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(),name="logout"), #LogoutView.as_view(template_name='AppUsuarios/logout.html)... esto me permite personalizar la pagina de logout, sino puedo mandarlo a otra desde settings.py LOGOUT_REDIRECT_URL
    path('editarPerfil/', editarPerfil, name='editarPerfil'),    
]