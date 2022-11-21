from datetime import datetime
from pydantic import BaseModel
from pydantic import Field

    
class SucursalesBase(BaseModel):
    """Extiende la clase BaseModel.

    Args:
        BaseModel (_type_): Clase a extender
    """
    nombre_sucursal: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example = "C.C aventura"
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
        example = '8360876'
    )
    nombre_encargado: str = Field(
        ...,
        example = "nombres apellidos"
    )
    horario_atencios: datetime =  Field(default=datetime.now())
    



class Sucursales(SucursalesBase):
    """Este modelo lo emplearemos como respuesta cuando necesitemos retornar la información de un usuario

    Args:
        UserBase (_type_): extiende la clase UserBase
    """
    id: int = Field(
        ...,
        example="5"
    )


class SucursalesRegister(SucursalesBase):
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