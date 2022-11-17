from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

    
class UserBase(BaseModel):
    """Extiende la clase BaseModel.

    Args:
        BaseModel (_type_): Clase a extender
    """
    correo: EmailStr = Field(
        ...,
        ejemplo = "mmmmm@hotmail.com"
    )
    nombre: str = Field(
        ...,
        min_length=3,
        max_length=50,
        ejemplo = "Nombre Completo"
    )
    direccion: str = Field(
        ...,
        example = 'calle 62 # 35 -42'
    )
    telefono: int = Field(
        ...,
        ejemplo = '3118974532'
    )



class User(UserBase):
    """Este modelo lo emplearemos como respuesta cuando necesitemos retornar la información de un usuario

    Args:
        UserBase (_type_): extiende la clase UserBase
    """
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    """
    La emplearemos como modelo cuando un usuario se quiera registrar.

    Args:
        UserBase (_type_): hereda UserBase
    """
    contrasena: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="min8max64"
    )