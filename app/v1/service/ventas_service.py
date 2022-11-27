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
        is_done = db_ventas.is_done,
        fecha = db_ventas.fecha,
        sucursales = db_ventas.sucursales

    )

def get_ventas(user: user_schema.User, is_done: bool = None):
    
    if is_done is None:
        ventas_by_user = VentasModel.filter(VentasModel.user_id == user.id).order_by(VentasModel.create_at.desc())
    else:
        ventas_by_user = VentasModel.filter((VentasModel.user_id  == user.id) & (VentasModel.is_done == is_done)).order_by(VentasModel.create_at.desc())
        
    list_ventas = []
    for ventas in ventas_by_user:
        list_ventas.append(
            ventas_schema.Ventas(
                id = ventas.id,
                title=ventas.title,
                producto=ventas.producto,
                cantidad=ventas.cantidad,
                fecha=ventas.fecha,
                usuario=ventas.usuario,
                sucursales=ventas.sucursales
            )
        )
        
    return list_ventas

def get_venta(venta_id: int, user: user_schema.User):
    venta = VentasModel.filter(
        (VentasModel.id == venta_id) & (VentasModel.user_id == user.id)
        ).get()
    
    return ventas_schema.Ventas(
        id = venta.id,
        title=venta.title,
        producto=venta.producto,
        cantidad=venta.cantidad,
        fecha=venta.fecha,
        usuario=venta.usuario,
        sucursales=venta.sucursales
    )

def update_status_task(is_done: bool, venta_id: int, user: user_schema.User):
    """" Actualiza el estado de las tareas

    Args:
        is_done (bool): indicará el nuevo estado de la tarea
        venta_id (int): id de venta guardada
        user (user_schema.User): usuario comprador

    Raises:
        HTTPException: excepcion para comprobar si la tarea existe o no.

    Returns:
        _type_:  valores actualizados
    """
    venta = VentasModel.filter(
        (VentasModel.id == venta_id) & ( VentasModel.user_id == user.id)
    ).first()
    
    if not venta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró el pedido"
        )
    
    venta.is_done = is_done
    venta.save()
    
    return ventas_schema.Ventas(
        id = venta.id,
        title=venta.title,
        producto=venta.producto,
        cantidad=venta.cantidad,
        fecha=venta.fecha,
        usuario=venta.usuario,
        sucursales=venta.sucursales
    ) 

def delete_task(task_id: int, user: user_schema.User):
    """Elimina ventas en caso de que estas sean canceladas, reciviendo un id del pedido y del usuario que
    lo realizo y si estos coinciden los elimina

    Args:
        venta_id (int): id de la venta
        user (user_schema.User): usuario que realizo la compra

    Raises:
        HTTPException: _description_
    """
    venta = VentasModel.filter((VentasModel.id == task_id) & (VentasModel.user_id == user.id)).first()

    if not venta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pedido no encontrado"
        )

    venta.delete_instance()


