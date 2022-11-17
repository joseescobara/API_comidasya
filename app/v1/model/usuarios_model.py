
import peewee

from app.v1.utils.db import db 


class User(peewee.Model):
    """
    Esta clase extiende de peewee.Model y en ella declaramos
     los campos que vamos a necesitar para modelar la tabla de Usuaios.

    Args:
        peewee.Model: clase que extendemos a nuestro modelo.
    """
    correo = peewee.CharField(unique=True, index=True)
    nombre = peewee.CharField(unique=True, index=True)
    contrasena = peewee.CharField()
    direccion = peewee.CharField()
    telefono = peewee.IntegerField()
    
    class Meta:
        """ contendrá la conexión a la base de datos.
        """
        database = db 
    
