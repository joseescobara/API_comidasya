
from enum import unique
import peewee

from app.v1.utils.db import db 


class User(peewee.Model):
    correo = peewee.CharField(unique=True, index=True)
    nombre = peewee.CharField(unique=True, index=True)
    contrasena = peewee.CharField()
    direccion = peewee.CharField()
    telefono = peewee.IntegerField()
    
    class Meta:
        database = db 
    
