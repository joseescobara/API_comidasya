from fastapi import HTTPException, status

from app.v1.schema import menus_schema
from app.v1.schema import user_schema

from app.v1.model.menu_model import Menu as MenuModel


def create_menus(menu: menus_schema.MenuCreate, user: user_schema.User):
    
    db_menu = MenuModel(
        tipo_pizza=menu.tipos_pizza,
         user=user.id
    )

    db_menu.save()

    return menus_schema.Menu(
        id = db_menu.id,
        tipos_pizza = db_menu.tipos_pizza,
        ingredientes = db_menu.ingredientes,
        tamaño=db_menu.tamaño,
        is_done=db_menu.is_done,
        bebidas=db_menu.bebidas,
        porciones=db_menu.porciones,
        precio=db_menu.precio
    )

def get_menus(user: user_schema.User, is_done: bool = None):
    
    if (is_done is None):
        menus_by_user = MenuModel.filter(MenuModel.user_id == user.id).order_by(MenuModel.create_at.desc())
    else:
        menus_by_user = MenuModel.filter((MenuModel.user_id  == user.id) & (MenuModel.is_done == is_done)).order_by(MenuModel.create_at.desc())
        
    list_menus = []
    for menus in menus_by_user:
        list_menus.append(
            menus_schema.Menu(
                id = menus.id,
                ingredientes= menus.ingredientes,
                tamaño = menus.tamaño,
                is_done= menus.is_done,
                bebidas=menus.bebidas,
                porciones=menus.porciones,
                precio=menus.precio,
                user=menus.user
            )
        )
        
    return list_menus

def get_menu(menu_id: int, user: user_schema.User):
    menu = MenuModel.filter(
        (MenuModel.id == menu_id) & (MenuModel.user_id == user.id)
        ).get()
    
    return menus_schema.Menu(
        id = menu.id,
        ingredientes= menu.ingredientes,
        tamaño = menu.tamaño,
        is_done= menu.is_done,
        bebidas=menu.bebidas,
        porciones=menu.porciones,
        precio=menu.precio,
        user=menu.user
    )



def update_status_menu(is_done: bool, menu_id: int, user: user_schema.User):
    """" Actualiza el estado de las Menu

    Args:
        is_done (bool): indicará el nuevo estado de la tarea
        venta_id (int): id de venta guardada
        user (user_schema.User): usuario comprador

    Raises:
        HTTPException: excepcion para comprobar si la tarea existe o no.

    Returns:
        _type_:  valores actualizados
    """
    menu = MenuModel.filter((MenuModel.id == menu_id) & ( MenuModel.user_id == user.id)).first()
    
    if not menu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró el menu"
        )
    
    menu.is_done = is_done
    menu.save()
    
    return menus_schema.Menu(
        id = menu.id,
        ingredientes= menu.ingredientes,
        tamaño = menu.tamaño,
        is_done= menu.is_done,
        bebidas=menu.bebidas,
        porciones=menu.porciones,
        precio=menu.precio,
        user=menu.user
    ) 



def delete_menu(menu_id: int, user: user_schema.User):
    """Elimina un menu en caso de que estos ya no esten disponibles .

    Args:
        venta_id (int): id de la venta
        user (user_schema.User): usuario que realizo la compra

    Raises:
        HTTPException: _description_
    """
    menu = MenuModel.filter((MenuModel.id == menu_id) & (MenuModel.user_id == user.id)).first()

    if not menu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="menu no encontrado"
        )

    menu.delete_instance()

