from fastapi import HTTPException, status

from passlib.context import CryptContext


from app.v1.model.user_model import User as UserModel
from app.v1.schema import user_schema
from app.v1.service.auth_service import get_password_hash



def create_user(user: user_schema.UserRegister):
    """Esta función me permite crear un usuario en la base de datos a través de un método post
    Args:
        user (user_schema.UserRegister): usuario a crear
    Raises:
        HTTPException: Error cuándo la petición no satisface las condiciones
    Returns:
        json: Usuario creado
    """
    
    get_user = UserModel.filter(
        (UserModel.correo == user.correo) | (UserModel.telefono == user.telefono)
        )
    if get_user:
        msg = "El correo ya está creado"
        if get_user.get().telefono == user.telefono:
            msg = "Telefono ya creado"
            
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = msg
        )
    
    db_user = UserModel(
        correo = user.correo,
        username = user.username,
        nombre = user.nombre,
        password = get_password_hash(user.password),
        direccion = user.direccion,
        telefono = user.telefono
        
    )
    db_user.save()
 
    return user_schema.User(
        id = db_user.id,
        correo=db_user.correo,
        username=db_user.username,
        nombre = db_user.nombre,
        password = db_user.password,
        direccion= db_user.direccion,
        telefono= db_user.telefono
    )