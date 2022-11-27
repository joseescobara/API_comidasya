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
        example = "mmmmm@hotmail.com"
    )
    nombre: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example = "Nombre Completo"
    )
    username: str = Field(
        ...,
        example = 'username11'
    )
    direccion: str = Field(
        ...,
        example = 'calle 62 # 35 -42'
    )
    telefono: int = Field(
        ...,
        example = '311897453'
    )




class User(UserBase):
    """ Valida los Id

    Args:
        UserBase (_type_): Herencia de UserBase
    """

    id: int = Field(
        ...,
        example = '5'
    )

class UserRegister(UserBase):
    """
    La emplearemos como modelo cuando un usuario se quiera registrar.

    Args:
        UserBase (_type_): hereda UserBase
    """
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="min8max64"
    )