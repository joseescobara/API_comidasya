# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class VentasCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=60,
        example="Pizza"
    )


class Ventas(VentasCreate):
    producto: int = Field(...)
    cantidad: int = Field(...)
    is_done: bool = Field(default=False)
    fecha: datetime = Field(default=datetime.now())
    usuario: int = Field(...)
    sucursales: int = Field(...)