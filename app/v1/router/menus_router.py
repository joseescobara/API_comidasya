from fastapi import APIRouter, Depends, Body
from fastapi import status

from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import menus_schema
from app.v1.service import menus_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user


router = APIRouter(prefix="/api/v1/menus")

@router.post(
    "/",
    tags=["menus"],
    status_code=status.HTTP_201_CREATED,
    response_model=menus_schema.Menu,
    dependencies=[Depends(get_db)]
)
def create_menus(menu: menus_schema.Menu = Body(...),
    current_user: User = Depends(get_current_user)):
    return menus_service.create_menus(menu, current_user)



@router.get(
    "/",
    tags=["menus"],
    status_code=status.HTTP_200_OK,
    response_model=List[menus_schema.Menu],
    dependencies= [Depends(get_db)]
)
def get_menus(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return menus_service.get_menus(current_user, is_done)

@router.get(
    "/{menu_id}",
    tags=["menu"],
    status_code=status.HTTP_200_OK,
    response_model=menus_schema.Menu,
    dependencies=[Depends(get_db)]
)
def get_menu(
    menu_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return menus_service.get_menus(menu_id, current_user)




@router.patch(
    "/{menu_id}/mark_done",
    tags = ["menu"],
    status_code=status.HTTP_200_OK,
    response_model=menus_schema.Menu,
    dependencies=[Depends(get_db)]
)
def mark_menu_done(
    menu_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return menus_service.update_status_task(True, menu_id, current_user)


@router.patch(
    "/{menu_id}/unmark_done",
    tags = ["menu"],
    status_code=status.HTTP_200_OK,
    response_model=menus_schema.Menu,
    dependencies=[Depends(get_db)]
)
def unmark_menu_done(
    menu_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return menus_service.update_status_task(False, menu_id, current_user)




@router.delete(
    "/{menu_id}/",
    tags=["menu"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_menu(
    menu_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    menus_service.delete_menu(menu_id, current_user)

    return {
        'msg': 'El menu a sido cancelado satisfactoriamente'
    }
