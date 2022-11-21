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
    state: Optional[bool] = Query(None)
):
    return ventas_service.get_ventas(state)

@router.get(
    "/{ventas_id}",
    tags=["ventas"],
    status_code=status.HTTP_200_OK,
    response_model=ventas_schema.Ventas,
    dependencies=[Depends(get_db)]
)
def get_or(
    ventas_id: int = Path(
        ...,
        gt=0
    )
):
    return ventas_service.get_ventas(ventas_id)


