from enum import unique
import peewee

from app.v1.utils.db import db 


class Domicilio(peewee.Model):
    producto = peewee.CharField(unique=True, index=True)
    cantidad = peewee.IntegerField()
    direccion = peewee.CharField()
    tipo_pago = peewee.CharField()
    usuario = peewee.ForeignKeyField()
    domiciliario = peewee.ForeignKeyField()
    tienda = peewee.ForeignKeyField()
    
    
    class Meta:
        database = db 