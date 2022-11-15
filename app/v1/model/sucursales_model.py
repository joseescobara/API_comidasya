from enum import unique
import peewee

from app.v1.utils.db import db 


class Domicilio(peewee.Model):
    nombre_sucursal = peewee.CharField(unique=True, index=True)
    direccion = peewee.CharField(index=True)
    nombre_encargado = peewee.CharField()
    horario_atencion = peewee.TimeField()
    