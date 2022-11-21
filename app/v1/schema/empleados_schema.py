from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

    
class EmpleadosBase(BaseModel):
    """Extiende la clase BaseModel.

    Args:
        BaseModel (_type_): Clase a extender
    """
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
    telefono: int = Field(
        ...,
        example = '3118974532'
    )
    cargo: str = Field(
        ...,
        example = 'mesero'
    )
    correo: EmailStr = Field(
        ...,
        example = "mmmmm@hotmail.com"
    )
    numero_cuenta: float = Field(
        ...,
        example = '765438753'
    )

    direccion: str = Field(
        ...,
        example = 'calle 62 # 35 -42'
    )
    telefono: int = Field(
        ...,
        example = '311897453'
    )
    sucursal: int = Field(
        ...,
        example='1'
    )



class Empleados(EmpleadosBase):
    """Este modelo lo emplearemos como respuesta cuando necesitemos retornar la información de un usuario

    Args:
        UserBase (_type_): extiende la clase UserBase
    """
    id: int = Field(
        ...,
        example="5"
    )


class EmpleadosRegister(EmpleadosBase):
    """
    La emplearemos como modelo cuando  se quiera registrar un nuevo empleado.

    Args:
        UserBase (_type_): hereda UserBase
    """
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="min8max64"
    )