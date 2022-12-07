from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarDatos/', views.registrarDatos),
    path('edicionRegistro/<codigoRFID>', views.edicionRegistro),
    path('editarRegistro/', views.editar_registro),
    path('consultarDatos/', views.consultar),
    path('eliminacionRegistro/<codigoRFID>', views.eliminar_registro),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
