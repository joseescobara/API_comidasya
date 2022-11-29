from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import Optional, List

from app.v1.schema import domicilios_schema
from app.v1.service import domicilios_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User


from app.v1.service.auth_service import get_current_user


router = APIRouter(prefix="/api/v1/domicilios")

@router.post(
    "/",
    tags=["domicilios"],
    status_code=status.HTTP_201_CREATED,
    response_model=domicilios_schema.Domicilios,
    dependencies=[Depends(get_db)]
)

def create_domicilios(domicilios: domicilios_schema.DomiciliosCreate = Body(...),
    current_user: User = Depends(get_current_user)
):
    """
    Crea las rutas para poder crear una domicilio.

    Args:
        domicilios: variable de DomiciliosCreate la cual es obligatoria.
        current_user: es el resultado de la funcion get_current_user 

    Returns:
        _type_: si es valido devuelve el domicilio, si no lo es devuelve un error con su respectiva explicacion
    """
    return domicilios_service.create_domicilio(domicilios, current_user)



@router.get(
    "/",
    tags=["domicilios"],
    status_code=status.HTTP_200_OK,
    response_model=List[domicilios_schema.Domicilios],
    dependencies= [Depends(get_db)]
)
def get_domicilios(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    """Crea las rutas para poder traer los domicilos segun su estado de realizado o no.

    Args:
        is_done (Optional[bool], optional): Estado del domicilio.
        current_user (User, optional): usuario que lo realiza

    Returns:
        _type_: lista de domicilios.
    """
    return domicilios_service.get_domicilio(current_user, is_done)

@router.get(
    "/{domicilios_id}",
    tags=["domicilios"],
    status_code=status.HTTP_200_OK,
    response_model=domicilios_schema.Domicilios,
    dependencies=[Depends(get_db)]
)
def get_domicilio(
    domicilio_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Crea una ruta para acceder a un solo domicilio.

    Args:
        domicilio_id (int, optional): id que distingue el domicilio que es requerido.
        current_user (User, optional): Autenticacion del usuario

    Returns:
        _type_: domicilio solicitado en caso de estar , de lo contrario un error.
    """
    return domicilios_service.get_domicilio(domicilio_id,current_user)



@router.patch(
    "/{domicilio_id}/mark_done",
    tags = ["domicilio"],
    status_code=status.HTTP_200_OK,
    response_model=domicilios_schema.Domicilios,
    dependencies=[Depends(get_db)]
)
def mark_domicilios_done(
    domicilio_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Cambia el estado del domicilio, en caso de una cancelacion o ya estar entregado.

    Args:
        domicilio_id (int, optional): id del domicilioespecifico.
        current_user (User, optional): usuario que lo realizo.

    Returns:
        _type_: actualizacion del estado.
    """
    return domicilios_service.update_status_task(True, domicilio_id, current_user)


@router.patch(
    "/{domicilios_id}/unmark_done",
    tags = ["domicilio"],
    status_code=status.HTTP_200_OK,
    response_model=domicilios_schema.Domicilios,
    dependencies=[Depends(get_db)]
)
def unmark_domicilios_done(
    domicilios_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Cambia estado del pedido, en caso de que se le haga un amodificacion y se quiera que vuelva estar activo.

    Args:
        domicilios_id (int, optional): id del domicilio
        current_user (User, optional): usuario autenticado

    Returns:
        _type_: estado actualizado del pedido.
    """
    return domicilios_service.update_status_domicilios(False, domicilios_id, current_user)



@router.delete(
    "/{domicilios_id}/",
    tags=["domicilios"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_domicilio(
    domicilio_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    """Borra un pedido en caso de que se quiera cancelar definitivamente.

    Args:
        domicilio_id (int, optional): id del domicilio.
        current_user (User, optional): usuario autenticado.

    Returns:
        _type_: mensage con la confirmacion de la cancelacion del pedido.
    """
    domicilios_service.delete_domicilio(domicilio_id, current_user)

    return {
        'msg': 'El pedido a sido cancelado satisfactoriamente'
    }
