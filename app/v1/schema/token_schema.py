from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    """ 
    usaremos para retornarle el token de autenticación y el tipo de autenticación 

    Args:
        BaseModel (_type_): _description_
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """ Almacenará el nombre de usuario en el token

    Args:
        BaseModel (_type_): _description_
    """
    username: Optional[str] = None