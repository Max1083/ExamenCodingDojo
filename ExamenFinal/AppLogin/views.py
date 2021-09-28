from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.db.models import Count
import bcrypt
from datetime import date
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
        request.session['user_name'] = usuario[0].nombre
        return redirect('travels')


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
    return redirect('inicio')


def logout(request):
    request.session.flush()
    return redirect('inicio')


def travels(request):
    viaj = Travels.objects.all()
    v = viaj.objects.filter(user=request.session['user_id'])
    print(v[0])
    context = {'viajes':Travels.objects.all().exclude(user=request.session['user_id']),
               'viajes2':Travels.objects.filter(user=request.session['user_id'])}
    return render(request,'travels.html',context)


def agregar(request):
    return render(request,'agregar.html')


def add(request):
    errores={}
    usuario= User.objects.filter(id=request.session['user_id'])
    print(usuario[0].id)
    if len(request.POST['destino']) == 0:
        errores['destino']='Debe ingresar un destino'
        
    if len(request.POST['descripcion'])==0:
        errores['descripcion']='Debe colocar una descripcion'
    
    if len(request.POST['fechini']) == 0:
        errores['fechini']='Debe seleccionar una fecha' 
    
    if len(request.POST['fechfin']) == 0 :
        errores['fechfin']='Debe seleccionar una fecha'    
    
    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return render(request, 'agregar.html')
    else:
        
        Travels.objects.create(        
        destino = request.POST['destino'],
        descripcion = request.POST['descripcion'],
        fechain = request.POST['fechini'],
        fechafn = request.POST['fechfin']
         ).user.add(usuario[0].id)
    return redirect('travels')
    
    
def destino(request,id):
    destino1 = Travels.objects.get(id = id)
 
    context ={
        'destino1':destino1,
        
    }
    return render(request,'destino.html', context)



def unirse(request):
    jo = Travels.objects.filter(id=request.POST['id'])
    print("***********************",jo,"***********************")    
    return render(request,'travels.html')