from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from app.v1.schema import sucursales_schema
from app.v1.service import sucursales_service


from app.v1.utils.db import get_db

router = APIRouter(prefix='/api/v1')

@router.post(
    '/sucursales/',
    tags = ['sucursales'],
    status_code=status.HTTP_201_CREATED,
    response_model=sucursales_schema.Sucursales,
    dependencies=[Depends(get_db)],
    summary="Sucursal creada"   
)
def create_sucursal(sucursal: sucursales_schema.SucursalesRegister = Body(...)):
    """Ejecuta la función create en service
    Args:
        user (user_schema.UserRegister, optional): Usuario a crear
    Returns:
        json: usuario creado
    """
    
    return sucursales_service.create_sucursal(sucursal)