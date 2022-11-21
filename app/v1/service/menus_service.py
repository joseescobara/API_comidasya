from fastapi import HTTPException, status

from app.v1.schema import menus_schema
from app.v1.schema import sucursales_schema

from app.v1.model.menu_model import Menu as MenuModel


def create_menu(menu: menus_schema.MenuCreate, sucursal: sucursales_schema.Sucursales):

    db_menu = MenuModel(
        tipo_pizza=menu.tipos_pizza,
        sucursal_id=sucursal.id
    )

    db_menu.save()

    return menus_schema.Menu(
        id = db_menu.id,
        tipos_pizza = db_menu.tipos_pizza,
        ingredientes = db_menu.ingredientes,
        tamaño=db_menu.tamaño,
        bebidas=db_menu.bebidas,
        porciones=db_menu.porciones,
        precio=db_menu.precio
    )