from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.inicio,name='inicio'),
    path('login',views.login,name='login'),
    path('registro',views.registro,name='registro'),
    path('logout',views.logout,name='logout'),
    path('travels',views.travels,name='travels'),
    path('travels/agregar',views.agregar,name='agregar'),
    path('add',views.add,name='add'),
    path('destino/<int:id>',views.destino,name='destino'),
    path('unirse', views.unirse, name='unirse'),
]