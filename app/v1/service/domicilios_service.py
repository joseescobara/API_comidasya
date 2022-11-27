from fastapi import HTTPException, status

from app.v1.schema import domicilios_schema
from app.v1.schema import user_schema
from app.v1.schema import sucursales_schema
from app.v1.schema import ventas_schema
from app.v1.schema import empleados_schema
from app.v1.model.domicilios_model import Domicilio as DomicilioModel


def create_domicilio(domicilios: domicilios_schema.DomiciliosCreate,
    user: user_schema.User,
    sucursales: sucursales_schema,
    domiciliario: empleados_schema,
    venta: ventas_schema
):

    db_domicilios = DomicilioModel(
        title=domicilios.title,
        user_id=user.id,
        sucursales_id=sucursales.id,
        domiciliario_id=domiciliario.id,
        venta_id=venta.id
    )

    db_domicilios.save()

    return ventas_schema.Ventas(
        id = db_domicilios.id,
        title = db_domicilios.title,
        venta = db_domicilios.venta,
        fecha = db_domicilios.fecha,
        direccion = db_domicilios.direccion,
        tipo_pago = db_domicilios.tipo_pago,
        is_done = db_domicilios.is_done

    )

def get_domicilios(user: user_schema.User, is_done: bool = None):
    
    if is_done is None:
        domicilios_by_user = DomicilioModel.filter(DomicilioModel.user_id == user.id).order_by(DomicilioModel.create_at.desc())
    else:
        domicilios_by_user = DomicilioModel.filter((DomicilioModel.user_id  == user.id) & (DomicilioModel.is_done == is_done)).order_by(DomicilioModel.create_at.desc())
        
    list_domicilios = []
    for domicilios in domicilios_by_user:
        list_domicilios.append(
            domicilios_schema.Ventas(
                id = domicilios.id,
                title=domicilios.title,
                venta = domicilios.venta,
                fecha = domicilios.fecha,
                direccion = domicilios.direccion,
                tipo_pago = domicilios.tipo_pago,
                is_done =domicilios.is_done,
                usuario = domicilios.usuarios,
                domiciliario = domicilios.domicilios,
                sucursales = domicilios.sucursales
            )
        )
        
    return list_domicilios

def get_domicilio(domicilio_id: int, user: user_schema.User):
    domicilio = DomicilioModel.filter(
        (DomicilioModel.id == domicilio_id) & (DomicilioModel.user_id == user.id)
        ).get()
    
    return domicilios_schema.Domicilios(
        id = domicilio.id,
        title=domicilio.title,
        venta = domicilio.venta,
        fecha = domicilio.fecha,
        direccion = domicilio.direccion,
        tipo_pago = domicilio.tipo_pago,
        is_done =domicilio.is_done,
        usuario = domicilio.usuarios,
        domiciliario = domicilio.domicilios,
        sucursales = domicilio.sucursales
    )

def update_status_task(is_done: bool, domicilio_id: int, user: user_schema.User):
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
    domicilio = DomicilioModel.filter(
        (DomicilioModel.id == domicilio_id) & ( DomicilioModel.user_id == user.id)
    ).first()
    
    if not domicilio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró el pedido"
        )
    
    domicilio.is_done = is_done
    domicilio.save()
    
    return domicilios_schema.Domicilios(
        id = domicilio.id,
        title=domicilio.title,
        venta = domicilio.venta,
        fecha = domicilio.fecha,
        direccion = domicilio.direccion,
        tipo_pago = domicilio.tipo_pago,
        is_done =domicilio.is_done,
        usuario = domicilio.usuarios,
        domiciliario = domicilio.domicilios,
        sucursales = domicilio.sucursales
    ) 

def delete_domicilio(task_id: int, user: user_schema.User):
    """Elimina ventas en caso de que estas sean canceladas, reciviendo un id del pedido y del usuario que
    lo realizo y si estos coinciden los elimina

    Args:
        venta_id (int): id de la venta
        user (user_schema.User): usuario que realizo la compra

    Raises:
        HTTPException: _description_
    """
    domicilio = DomicilioModel.filter((DomicilioModel.id == task_id) & (DomicilioModel.user_id == user.id)).first()

    if not domicilio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pedido no encontrado"
        )

    domicilio.delete_instance()