from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import Optional, List

from app.v1.schema import menus_schema
from app.v1.service import menus_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.schema.sucursales_schema import Sucursales

from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix="/api/v1/menus")

@router.post(
    "/",
    tags=["menus"],
    status_code=status.HTTP_201_CREATED,
    response_model=menus_schema.Menu,
    dependencies=[Depends(get_db)]
)
def create_menus(Menus: menus_schema.Menu = Body(...),
    current_user: User = Depends(get_current_user)
):
    return menus_service.create_menus(Menus, current_user)

@router.get(
    "/",
    tags=["menus"],
    status_code=status.HTTP_200_OK,
    response_model=List[menus_schema.Menu],
    dependencies= [Depends(get_db)]
)
def get_menus(
    state: Optional[bool] = Query(None)
):
    return menus_service.get_ventas(state)

@router.get(
    "/{menus_id}",
    tags=["ventas"],
    status_code=status.HTTP_200_OK,
    response_model=menus_schema.Menu,
    dependencies=[Depends(get_db)]
)
def get_or(
    menus_id: int = Path(
        ...,
        gt=0
    )
):
    return menus_service.get_menus(menus_id)


