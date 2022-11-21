from fastapi import HTTPException, status

from passlib.context import CryptContext


from app.v1.model.sucursales_model import Sucursales as SucursalesModel
from app.v1.schema import sucursales_schema
from app.v1.service.auth_service import get_password_hash


def create_sucursal(sucursal: sucursales_schema.SucursalesRegister):
    """Esta función me permite crear el registro de una sucursal  en la base de datos a través de un método post
    Args:
        user (user_schema.UserRegister): sucursal a crear
    Raises:
        HTTPException: Error cuándo la petición no satisface las condiciones
    Returns:
        json: Sucursal creada
    """
    
    get_sucursal = SucursalesModel.filter(
        (SucursalesModel.direccion == sucursal.direccion) | (SucursalesModel.telefono == sucursal.telefono)
        )
    if get_sucursal:
        msg = "La sucursal ya está creada"
        if get_sucursal.get().telefono == sucursal.telefono:
            msg = "Telefono ya registrado"
            
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = msg
        )
    
    db_sucursales = SucursalesModel(
        nombre_sucursal = sucursal.nombre_sucursal,
        username = sucursal.username,
        password = get_password_hash(sucursal.password),
        direccion = sucursal.direccion,
        telefono = sucursal.telefono,
        nombre_encargado = sucursal.nombre_encargado,
        horario_atencion = sucursal.horario_atencios
        
    )
    db_sucursales.save()
 
    return sucursales_schema.Sucursales(
        id = db_sucursales.id,
        nombre_sucursal = db_sucursales.nombre_sucursal,
        username = db_sucursales.username,
        password = db_sucursales.password,
        direccion= db_sucursales.direccion,
        telefono= db_sucursales.telefono,
        nombre_encargado = db_sucursales.nombre_encargado,
        horario_atencios=db_sucursales.horario_atencion

    )