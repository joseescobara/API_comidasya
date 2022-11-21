from datetime import datetime
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
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()
    direccion = peewee.CharField(index=True)
    telefono = peewee.IntegerField(unique=True, index=True)
    nombre_encargado = peewee.CharField(unique=True)
    horario_atencion = peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 