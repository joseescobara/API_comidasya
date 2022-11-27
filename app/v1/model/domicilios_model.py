from datetime import datetime

from enum import unique
import peewee

from app.v1.utils.db import db 
from .user_model import User
from .empleados_model import Empleados
from .sucursales_model import Sucursales
from .ventas_model import Ventas


class Domicilio(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Domicilios.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """
    title = peewee.CharField()
    venta = peewee.ForeignKeyField(Ventas, backref="ventas")
    fecha = peewee.DateTimeField(default=datetime.now)
    direccion = peewee.CharField(unique=True, index=True)
    tipo_pago = peewee.CharField()
    is_done = peewee.BooleanField(default=False)
    usuario = peewee.ForeignKeyField(User, backref="usuario")
    domiciliario = peewee.ForeignKeyField(Empleados, backref="domiciliario" )
    sucursales = peewee.ForeignKeyField(Sucursales, backref="sucursales" )
    
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 