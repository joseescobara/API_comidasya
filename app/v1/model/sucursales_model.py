from enum import unique
import peewee

from app.v1.utils.db import db 


class Sucursales(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Sucursales.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """
    nombre_sucursal = peewee.CharField(unique=True, index=True)
    direccion = peewee.CharField(index=True)
    nombre_encargado = peewee.CharField()
    horario_atencion = peewee.TimeField()
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 