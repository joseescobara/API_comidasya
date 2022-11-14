from enum import unique
import peewee

from app.v1.utils.db import db 


class Menu(peewee.Model):
    tipos_pizza = peewee.CharField(index=True)
    ingredientes = peewee.CharField()
    tamaño = peewee.CharField()
    bebidas = peewee.CharField()
    porciones = peewee.CharField()
    precio = peewee.IntegerField()
    class Meta:
        database = db 