from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import Optional, List

from app.v1.schema import ventas_schema
from app.v1.service import ventas_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.schema.sucursales_schema import Sucursales
from app.v1.schema.menus_schema import Menu

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
    current_user: User = Depends(get_current_user)
):
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
    return ventas_service.get_venta(ventas_id)


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
    ventas_service.delete_venta(venta_id, current_user)

    return {
        'msg': 'El pedido a sido cancelado satisfactoriamente'
    }