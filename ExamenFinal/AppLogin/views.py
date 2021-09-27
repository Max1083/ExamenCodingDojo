from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.db.models import Count
import bcrypt
from .models import *

# Create your views here.
def inicio(request):
    
    return render(request,'inicio.html')

def login(request):
    usuario = User.objects.filter(username=request.POST['lusername'].lower())
    errores = User.objects.validar_login(request.POST['lpassword'],usuario)
    print(usuario)
    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('inicio')
    else:
        request.session['user_id'] = usuario[0].id
        request.session['user_name'] = usuario[0].username
        return redirect('index')


def registro(request):
    #validacion de parametros
    errors = User.objects.validadorBasico(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('inicio')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        
        rol = 2
        if User.objects.all().count() == 0:
            rol = 1

        #crear usuario
        User.objects.create(
            username=request.POST['username'],
            nombre=request.POST['nombre'],
            email=request.POST['email'],
            password=password,
            rol=rol,
        )
        #request.session['user_id'] = user.id
        #retornar mensaje de creacion correcta
        msg="Usuario creado exitosamente!"
        messages.success(request, msg)
    return redirect('index')


def logout(request):
    request.session.flush()
    return redirect('inicio')


def index(request):
    return render(request,'index.html')