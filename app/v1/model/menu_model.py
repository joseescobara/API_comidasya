
import peewee
from .user_model import User
from .sucursales_model import Sucursales
from app.v1.utils.db import db 



class Menu(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Menus.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """
    tipos_pizza = peewee.CharField()
    ingredientes = peewee.CharField()
    tamaño = peewee.CharField()
    is_done = peewee.BooleanField(default=False)
    bebidas = peewee.CharField()
    porciones = peewee.IntegerField()
    precio = peewee.IntegerField()
    sucursales = peewee.ForeignKeyField(Sucursales, backref="sucursales")
    user = peewee.ForeignKeyField(User, backref="usuarios")
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 