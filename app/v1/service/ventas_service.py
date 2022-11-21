from fastapi import HTTPException, status

from app.v1.schema import ventas_schema
from app.v1.schema import user_schema
from app.v1.schema import sucursales_schema
from app.v1.schema import menus_schema
from app.v1.model.ventas_model import Ventas as VentasModel


def create_ventas(ventas: ventas_schema.VentasCreate,
    user: user_schema.User,
    sucursales: sucursales_schema,
    menus: menus_schema
):

    db_ventas = VentasModel(
        title=ventas.title,
        user_id=user.id,
        sucursales_id=sucursales.id,
        menus_id=menus.id
    )

    db_ventas.save()

    return ventas_schema.Ventas(
        id = db_ventas.id,
        title = db_ventas.title,
        producto = db_ventas.producto,
        cantidad = db_ventas.cantidad,
        fecha = db_ventas.fecha,
        sucursales = db_ventas.sucursales

    )