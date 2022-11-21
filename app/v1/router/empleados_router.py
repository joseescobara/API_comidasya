from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import  empleados_schema
from app.v1.service import empleados_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/empleados/",
    tags=["empleados"],
    status_code=status.HTTP_201_CREATED,
    response_model=empleados_schema.Empleados,
    dependencies=[Depends(get_db)],
    summary="Crear nuevo empleado"
)
def create_empleados(empleados: empleados_schema.EmpleadosRegister = Body(...)):
    """Crea un nuevo perfil para un empleado

    Args:
    La app puede recibir los siguientes campos en un json.
    - nombre = nombre del empleado
    telefono = numero de telefono del empleado
    cargo = cargo en el que se desempeñara el empleado
    correo = correo electronico
    numero_cuenta = numero de cuenta a la cual se le consignara su sueldo
    contrasena = contraseña
    direccion = direccion de residencia
    sucursal = sucursal del restaurante donde trabaja

    Returns:
        _type_: informacion del empleado
    """
    return empleados_service.create_empleados(empleados)