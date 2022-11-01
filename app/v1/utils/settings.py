#aquí vamos a crear las variables de entorno

import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()      #estamos cargando las variables de entorno que están guardadas en .env

class Settings(BaseSettings):
    #esto me permite acceder a las configuraciones de conexión a la bd que están almacenadas en la clase settings
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    de_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')