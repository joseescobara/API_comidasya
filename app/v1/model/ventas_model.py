from enum import unique
import peewee

from app.v1.utils.db import db 

class Ventas(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Ventas.

    Args:
        peewee (_type_): _description_
    """
    producto = peewee.CharField()
    cantidad = peewee.IntegerField()
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 