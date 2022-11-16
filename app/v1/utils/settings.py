#aquí vamos a crear las variables de entorno

import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()     

class Settings(BaseSettings):
    """
    Esta  clase extiende BaseSetting y me permite acceder a las configuraciones de conexión a la bd 
    que están almacenadas en la clase settings

    Args:
        BaseSettings (_type_): _description_
    """
    
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')