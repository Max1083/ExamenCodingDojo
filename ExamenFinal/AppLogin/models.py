from django.db import models
import re
import bcrypt

# Create your models here.
errores={}
class UserManager(models.Manager):
    def validadorBasico(self,data):
        if len(User.objects.filter(username=data['username'])) > 0:
            errores['existe'] = "Username ya registrado..!!!"
        else:
            if len(data['username']) == 0:
                errores['username'] = "Nombre de usuario obligatorio"
            if len(data['nombre']) == 0:
                errores['nombre'] = "Nombre es obligatorio"
            EMAIL = re.compile(
                r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL.match(data['email']):
                errores['email'] = "email invalido"
            if len(data['password']) < 6:
                errores['password'] = "Password debe ser mayor a 6 caracteres"

            val_pass = self.comparar_password(data['password'],data['repassword'])
            if len(val_pass) > 0:
                errores['password'] = val_pass
        return errores
    
    
    def encriptar(self, password):
        password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        return password.decode('utf-8')   
    
    
    
    def validar_login(self, password, usuario ):
        if len(usuario) > 0:
            pw_hash = usuario[0].password

            if bcrypt.checkpw(password.encode(), pw_hash.encode()) is False:
                errores['pass_incorrecto'] = "password es incorrecto"
        else:
            errores['usuario_invalido'] = "Usuario no existe"
        return errores
    
    
    
    def comparar_password(self,password, repassword):
        if password != repassword:
            return "Password no son iguales"
        else:
            return ""
        
        

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)    
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    rol = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    
class Travels(models.Model):
    id= models.AutoField(primary_key=True)
    user=models.ManyToManyField(User,related_name="travels")
    destino=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=255)
    fechain=models.DateField()
    fechafn=models.DateField()
    