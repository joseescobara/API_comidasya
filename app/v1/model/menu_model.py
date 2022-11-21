
import peewee

from .sucursales_model import Sucursales
from app.v1.utils.db import db 


class Menu(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Menus.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """
    tipos_pizza = peewee.CharField(index=True)
    ingredientes = peewee.CharField()
    tamaño = peewee.CharField()
    bebidas = peewee.CharField()
    porciones = peewee.IntegerField()
    precio = peewee.IntegerField()
    sucursal = peewee.ForeignKeyField(Sucursales, backref="sucursales")
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 