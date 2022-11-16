from enum import unique
import peewee

from app.v1.utils.db import db 


class Domicilio(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Domicilios.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """
    producto = peewee.CharField(unique=True, index=True)
    cantidad = peewee.IntegerField()
    direccion = peewee.CharField(unique=True, index=True)
    tipo_pago = peewee.CharField()
    usuario = peewee.ForeignKeyField()
    domiciliario = peewee.ForeignKeyField()
    tienda = peewee.ForeignKeyField()
    
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 