from datetime import datetime

import peewee

from app.v1.utils.db import db 
from .sucursales_model import Sucursales


class Empleados(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Empleados.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """

    nombre = peewee.CharField(index=True)
    telefono = peewee.IntegerField()
    cargo = peewee.CharField(index=True)
    turno = peewee.TimeField(index=True)
    correo = peewee.CharField(unique=True, index=True)
    numero_cuenta = peewee.IntegerField(unique=True, index=True)
    contrasena = peewee.CharField(unique=True, index=True)
    direccion = peewee.CharField()
    sucursal = peewee.ForeignKeyField(Sucursales,  backref="empleados")
    
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 