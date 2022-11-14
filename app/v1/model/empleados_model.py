from enum import unique
import peewee

from app.v1.utils.db import db 


class User(peewee.Model):
    nombre = peewee.CharField(unique=True, index=True)
    telefono = peewee.IntegerField()
    cargo = peewee.CharField(index=True)
    turno = peewee.TimeField(index=True)
    correo = peewee.CharField(unique=True, index=True)
    numero_cuenta = peewee.IntegerField()
    contrasena = peewee.CharField()
    direccion = peewee.CharField()
    
    
    class Meta:
        database = db 