# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel
from pydantic import Field


class MenuCreate(BaseModel):
    """
    extiende la clase BaseModel, sera utilizado cuando se nos pida una venta o un alista de ventas.
    Args:
        BaseModel (_type_): clase de pydantic a extender.
    """
    tipos_pizza: str = Field(
        ...,
        min_length=1,
        max_length=60,
        example="pizza hawaiana"
    )


class Menu(MenuCreate):
    id: int = Field(...)
    ingredientes: str = Field(...)
    tamaño: str = Field(...)
    is_done: bool = Field(default=False)
    bebidas: str = Field(...)
    porciones: int = Field(...)
    precio: int = Field(...)