from django.shortcuts import render, redirect
from .models import Registro, Oficina, Ingreso
from django.contrib import messages
import json, time
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def login(request):
    return render(request, 'login.html')
    

def registro(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'registro.html', context)

def consultar(request):
    data = request.POST.get('Rfid')
    data = Ingreso.objects.filter(codigoRFID = data).order_by('-data_time')[:8]
    return render(request, 'ingresos.html', {'data':data})


def home(request):
    registroListado = Registro.objects.all()
    messages.success(request, '¡Registros listados!')

    if request.method == "POST":
        request_data = json.dumps(request.GET)
        print(request_data)
        print(type(request_data))
        # print(request.GET)

    return render(request, "vistaRegistro.html", {"registros": registroListado})

@login_required
def registrarDatos(request):
    codigorfid=request.POST['Rfid']
    nombre=request.POST['Nombre']
    apellido=request.POST['Apellido']
    cc=request.POST['Cc']
    idoficina=request.POST['idOficina']
    if idoficina == '1':
        oficina = 'Despacho'
    elif idoficina == '2':
        oficina = 'Comunicaciones'
    elif idoficina == '3':
        oficina = 'Control Disciplinario Interno'
    elif idoficina == '4':
        oficina = 'Desarrollo Económico'
    elif idoficina == '5':
        oficina = 'Educación'
    elif idoficina == '6':
        oficina = 'Evaluación y Control'
    elif idoficina == '7':
        oficina = 'Familia'
    elif idoficina == '8':
        oficina = 'General'
    elif idoficina == '9':
        oficina = 'Gobierno'
    elif idoficina == '10':
        oficina = 'Hacienda'
    elif idoficina == '11':
        oficina = 'Infraestructura'
    elif idoficina == '12':
        oficina = 'Jurídica'
    elif idoficina == '13':
        oficina = 'Medio Ambiente'
    elif idoficina == '14':
        oficina = 'Movilidad'
    elif idoficina == '15':
        oficina = 'Participación Ciudadana'
    elif idoficina == '16':
        oficina = 'Planeación'
    elif idoficina == '17':
        oficina = 'Privada'
    elif idoficina == '18':
        oficina = 'Salud y Protección Social'
    elif idoficina == '19':
        oficina = 'Seguridad'
    elif idoficina == '20':
        oficina = 'Servicios Administrativos'
    elif idoficina == '21':
        oficina = 'TIC'
    elif idoficina == '22':
        oficina = 'Vivienda y Hábitat'

    registro = Registro.objects.create(codigoRFID=codigorfid, nombre=nombre, apellido=apellido, cc=cc)
    regoficina = Oficina.objects.create(idoficina=idoficina, oficina=oficina)
    # oficinaregistro = RegistroOficina(codigorfid, idoficina)
    # oficinaregistro.save()
    
    messages.success(request, '¡Registrado correctamente!')
    # registro = Registro.objects.filter(codigoRFID=codigorfid)
    print(json.dumps(request.POST))
    return redirect('/')

def oficinas(request):
    listaOficinas = Oficina.objects.all()
    data = {
        'titulo':'Oficinas',
        'oficinasListadas':listaOficinas
    }
    return render(request,"vistaOficina.html", data)

@login_required
def edicionRegistro(request, codigoRFID):
    registro = Registro.objects.get(codigoRFID=codigoRFID)
    return render(request, "edicionRegistro.html", {"registro":registro})

@login_required
def editar_registro(request):
    codigorfid=request.POST['Rfid']
    nombre=request.POST['Nombre']
    apellido=request.POST['Apellido']
    cc=request.POST['Cc']
    idoficina=request.POST['idOficina']
    if idoficina == '1':
        oficina = 'Despacho'
    elif idoficina == '2':
        oficina = 'Comunicaciones'
    elif idoficina == '3':
        oficina = 'Control Disciplinario Interno'
    elif idoficina == '4':
        oficina = 'Desarrollo Económico'
    elif idoficina == '5':
        oficina = 'Educación'
    elif idoficina == '6':
        oficina = 'Evaluación y Control'
    elif idoficina == '7':
        oficina = 'Familia'
    elif idoficina == '8':
        oficina = 'General'
    elif idoficina == '9':
        oficina = 'Gobierno'
    elif idoficina == '10':
        oficina = 'Hacienda'
    elif idoficina == '11':
        oficina = 'Infraestructura'
    elif idoficina == '12':
        oficina = 'Jurídica'
    elif idoficina == '13':
        oficina = 'Medio Ambiente'
    elif idoficina == '14':
        oficina = 'Movilidad'
    elif idoficina == '15':
        oficina = 'Participación Ciudadana'
    elif idoficina == '16':
        oficina = 'Planeación'
    elif idoficina == '17':
        oficina = 'Privada'
    elif idoficina == '18':
        oficina = 'Salud y Protección Social'
    elif idoficina == '19':
        oficina = 'Seguridad'
    elif idoficina == '20':
        oficina = 'Servicios Administrativos'
    elif idoficina == '21':
        oficina = 'TIC'
    elif idoficina == '22':
        oficina = 'Vivienda y Hábitat'

    registro = Registro.objects.get(codigoRFID=codigorfid)
    registro.nombre = nombre
    registro.apellido = apellido
    registro.cc = cc
    registro.idoficina = idoficina
    registro.oficina = oficina
    registro.save()

    messages.success(request, '¡Registro editado correctamente!')

    return redirect('/')

@login_required
def eliminar_registro(request, codigoRFID):
    registro = Registro.objects.get(codigoRFID=codigoRFID)
    registro.delete()

    messages.success(request, '¡Registro eliminado!')

    return redirect('/')