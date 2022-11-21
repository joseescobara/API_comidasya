from fastapi import HTTPException, status

from passlib.context import CryptContext


from app.v1.model.empleados_model import Empleados as EmpleadosModel
from app.v1.schema import empleados_schema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(contraseña):
    return pwd_context.hash(contraseña)


def create_empleados(empleados: empleados_schema.EmpleadosRegister):
    """Esta función me permite crear un usuario en la base de datos a través de un método post.
    Args:
        user (user_schema.UserRegister): usuario a crear
    Raises:
        HTTPException: Error cuándo la petición no satisface las condiciones
    Returns:
        json: Usuario creado
    """
    
    get_empleados = EmpleadosModel.filter(
        (EmpleadosModel.correo == empleados.correo) | (EmpleadosModel.numero_cuenta == empleados.numero_cuenta)
        )
    if get_empleados:
        msg = "El correo ya está creado"
        if get_empleados.get().numero_cuenta == empleados.numero_cuenta:
            msg = "Cuenta ya existente"
            
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = msg
        )
    
    db_empleados = EmpleadosModel(
        nombre = empleados.nombre,
        username = empleados.username,
        telefono = empleados.telefono,
        cargo = empleados.cargo,
        correo = empleados.correo,
        numero_cuenta = empleados.numero_cuenta,
        password = empleados.password,
        direccion = empleados.direccion,
        sucursal = empleados.sucursal
        
    )
    db_empleados.save()
 
    return empleados_schema.Empleados(
        id = db_empleados.id,
        nombre = db_empleados.nombre,
        username = db_empleados.username,
        telefono = db_empleados.telefono,
        cargo = db_empleados.cargo,
        correo = db_empleados.correo,
        numero_cuenta = db_empleados.numero_cuenta,
        password = db_empleados.password,
        direccion = db_empleados.direccion,
        sucursal = db_empleados.telefono
    )