from datetime import datetime

from enum import unique
import peewee

from .user_model import User
from .sucursales_model import Sucursales
from .menu_model import Menu

from app.v1.utils.db import db 

class Ventas(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Ventas.

    Args:
        peewee (_type_): _description_
    """
    producto = peewee.ForeignKeyField(Menu, backref="ordenador")
    cantidad = peewee.IntegerField()
    fecha = peewee.DateTimeField(default=datetime.now)
    usuario = peewee.ForeignKeyField(User, backref="ordenador")
    sucursales = peewee.ForeignKeyField(Sucursales, backref="sucursales" )

    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db