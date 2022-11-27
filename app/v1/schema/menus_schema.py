# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel
from pydantic import Field


class MenuCreate(BaseModel):
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