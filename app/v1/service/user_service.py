from fastapi import HTTPException, status

from passlib.context import CryptContext


from app.v1.model.user_model import User as UserModel
from app.v1.schema import user_schema




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
        msg = "El email ya está creado"
        if get_user.get().telefono == user.telefono:
            msg = "Telefono ya creado"
            
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail = msg
        )
    
    db_user = UserModel(
        correo = user.correo,
        nombre = user.nombre,
        contrasena = user.contrasena,
        direccion = user.direccion,
        telefono = user.telefono
        
    )
    db_user.save()
 
    return user_schema.User(
        id = db_user.id,
        correo=db_user.correo,
        nombre = db_user.nombre,
        contrasena = db_user.contrasena,
        direccion= db_user.direccion,
        telefono= db_user.telefono
    )