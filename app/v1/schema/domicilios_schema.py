# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class DomiciliosCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=60,
        example="Pizza"
    )


class Domicilios(DomiciliosCreate):
    venta: int = Field(...)
    fecha: datetime = Field(default=datetime.now)
    direccion: str = Field(unique=True, index=True)
    tipo_pago: str = Field()
    is_done: bool = Field(default=False)
    usuario: int = Field(...)
    domiciliario: int = Field(...)
    sucursales: int = Field(...)
    