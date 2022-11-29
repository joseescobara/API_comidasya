from fastapi import HTTPException, status

from app.v1.schema import domicilios_schema
from app.v1.schema import user_schema
#from app.v1.schema import sucursales_schema
from app.v1.schema import ventas_schema
#from app.v1.schema import empleados_schema
from app.v1.model.domicilios_model import Domicilio as DomicilioModel


def create_domicilio(domicilios: domicilios_schema.DomiciliosCreate, user: user_schema.User):
    """
    Esta función me permite crear el registro de una domicilios en la base de datos a través de el método post

    Args:
        domicilios: Datos de los domicilios solicitados
        user (user_schema.User): usuario que realiza el pedido

    Returns:
        _type_: informacion del domicilio.
    """

    db_domicilios = DomicilioModel(
        title=domicilios.title,
        user_id=user.id  
    )

    db_domicilios.save()

    return ventas_schema.Ventas(
        id = db_domicilios.id,
        title = db_domicilios.title,
        fecha = db_domicilios.fecha,
        direccion = db_domicilios.direccion,
        tipo_pago = db_domicilios.tipo_pago,
        is_done = db_domicilios.is_done

    )



def get_domicilios(user: user_schema.User, is_done: bool = None):
    """Trae los domicilios pendientes.

    Args:
        user (user_schema.User): usuario que pide el domicilio
        is_done (bool, optional): estado del domicilio, en que false es que no a sido entregado.

    Returns:
        _type_: lista de domicilios solicitados
    """
    if (is_done is None):
        domicilios_by_user = DomicilioModel.filter(DomicilioModel.user_id == user.id).order_by(DomicilioModel.create_at.desc())
    else:
        domicilios_by_user = DomicilioModel.filter((DomicilioModel.user_id  == user.id) & (DomicilioModel.is_done == is_done)).order_by(DomicilioModel.create_at.desc())
        
    list_domicilios = []
    for domicilios in domicilios_by_user:
        list_domicilios.append(
            domicilios_schema.Domicilios(
                id = domicilios.id,
                title=domicilios.title,
                venta = domicilios.venta,
                fecha = domicilios.fecha,
                direccion = domicilios.direccion,
                tipo_pago = domicilios.tipo_pago,
                is_done =domicilios.is_done
            )
        )
        
    return list_domicilios

def get_domicilio(domicilio_id: int, user: user_schema.User):
    """Trae un domicilio en especifico

    Args:
        domicilio_id (int): domicilios requeridos
        user (user_schema.User): usuario que la realizo

    Raises:
        HTTPException: error en caso de no estar registrado.

    Returns:
        _type_: el domicilio en caso de ser encontrada, o un error en caso de que no la encuentre.
    """
    domicilio = DomicilioModel.filter(
        (DomicilioModel.id == domicilio_id) & (DomicilioModel.user_id == user.id)
        ).get()
    if not domicilio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existe el domicilio"
        )
    
    return domicilios_schema.Domicilios(
        id = domicilio.id,
        title=domicilio.title,
        venta = domicilio.venta,
        fecha = domicilio.fecha,
        direccion = domicilio.direccion,
        tipo_pago = domicilio.tipo_pago,
        is_done =domicilio.is_done
    )

def update_status_domicilios(is_done: bool, domicilio_id: int, user: user_schema.User):
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
        is_done =domicilio.is_done
    ) 



def delete_domicilio(domicilio_id: int, user: user_schema.User):
    """Elimina ventas en caso de que estas sean canceladas, reciviendo un id del pedido y del usuario que
    lo realizo y si estos coinciden los elimina

    Args:
        venta_id (int): id de la venta
        user (user_schema.User): usuario que realizo la compra

    Raises:
        HTTPException: _description_
    """
    domicilio = DomicilioModel.filter((DomicilioModel.id == domicilio_id) & (DomicilioModel.user_id == user.id)).first()

    if not domicilio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pedido no encontrado"
        )

    domicilio.delete_instance()