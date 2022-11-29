from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import Optional, List

from app.v1.schema import ventas_schema
from app.v1.service import ventas_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User

from app.v1.service.auth_service import get_current_user


router = APIRouter(prefix="/api/v1/ventas")

@router.post(
    "/",
    tags=["ventas"],
    status_code=status.HTTP_201_CREATED,
    response_model=ventas_schema.Ventas,
    dependencies=[Depends(get_db)]
)

def create_ventas(ventas: ventas_schema.Ventas = Body(...),
    current_user: User = Depends(get_current_user)):
    """
    Crea las rutas para poder crear una venta.

    Args:
        ventas:variable de VentasCreate la cual es obligatoria.
        current_user: es el resultado de la funcion get_current_user 

    Returns:
        _type_: si es valido devuelve la venta, si no lo es devuelve un error con su respectiva explicacion
    """
    return ventas_service.create_ventas(ventas, current_user)

@router.get(
    "/",
    tags=["ventas"],
    status_code=status.HTTP_200_OK,
    response_model=List[ventas_schema.Ventas],
    dependencies= [Depends(get_db)]
)
def get_ventas(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    """Crea las rutas para poder traer los ventas segun su estado de realizado o no.

    Args:
        is_done (Optional[bool], optional): Estado de la venta.
        current_user (User, optional): usuario que la realiza.

    Returns:
        _type_: lista de ventas.
    """
    return ventas_service.get_ventas(current_user, is_done)

@router.get(
    "/{venta_id}",
    tags=["ventas"],
    status_code=status.HTTP_200_OK,
    response_model=ventas_schema.Ventas,
    dependencies=[Depends(get_db)]
)

def get_venta(
    ventas_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Crea una ruta para acceder ana sola venta.

    Args:
        domicilio_id (int, optional): id que distingue la venta que es requerida.
        current_user (User, optional): Autenticacion del usuario

    Returns:
        _type_: Venta solicitado en caso de estar , de lo contrario un error.
    """
    return ventas_service.get_venta(ventas_id, current_user)


@router.patch(
    "/{venta_id}/mark_done",
    tags = ["venta"],
    status_code=status.HTTP_200_OK,
    response_model=ventas_schema.Ventas,
    dependencies=[Depends(get_db)]
)
def mark_venta_done(
    venta_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Cambia el estado de la venta, en caso de una cancelacion o ya estar entregada.

    Args:
        domicilio_id (int, optional): id de la venta.
        current_user (User, optional): usuario que lo realizo.

    Returns:
        _type_: actualizacion del estado.
    """
    return ventas_service.update_status_task(True, venta_id, current_user)


@router.patch(
    "/{venta_id}/unmark_done",
    tags = ["venta"],
    status_code=status.HTTP_200_OK,
    response_model=ventas_schema.Ventas,
    dependencies=[Depends(get_db)]
)
def unmark_venta_done(
    venta_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Cambia estado de la venta, en caso de que se le haga una modificacion y se quiera que vuelva estar activo.

    Args:
        venta_id (int, optional): id de la venta
        current_user (User, optional): usuario autenticado

    Returns:
        _type_: estado actualizado del pedido.
    """
    return ventas_service.update_status_task(False, venta_id, current_user)

@router.delete(
    "/{venta_id}/",
    tags=["venta"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_venta(
    venta_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Borra una venta en caso de que se quiera cancelar definitivamente.

    Args:
        venta_id (int, optional): id de la venta.
        current_user (User, optional): usuario autenticado.

    Returns:
        _type_: mensage con la confirmacion de la cancelacion del pedido.
    """
    ventas_service.delete_venta(venta_id, current_user)

    return {
        'msg': 'El pedido a sido cancelado satisfactoriamente'
    }