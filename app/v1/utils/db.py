#me va permitir interactuar con la base de datos

import peewee

from contextvars import ContextVar #esta librería me va permitir trabajar con las variables de configuración
from fastapi import Depends

from app.v1.utils.settings import Settings

settings = Settings() #este objeto tiene las variables de conexión


DB_NAME= settings.db_name
DB_USER= settings.db_user
DB_PASS= settings.de_pass
DB_HOST= settings.db_host
DB_PORT= settings.db_port #variables de conexión


#vamos a crear un json donde vamos a guardar el estado de la conexión

db_state_default = {
    "closed" : None,
    "conn": None,
    "ctx": None,
    "transactions": None
}

db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("state", db_state)
        super().__init__(**kwargs)
    
    def __setattr__(self, name, value):
        self._state.get()[name] = value
    
    def __getattr__(self, name):
        return self._state.get()[name]
 
#aquí creo la conexión a la base de datos de postgress   
db = peewee.PostgresqlDatabase(
    DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)


db._state = PeeweeConnectionState() #estado de conexión

print(f'este es el estado de la conexión {db._state}')
async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()

def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect() #mantener conexión abierta hasta que se cierre la aplicación
        yield
    finally:
        if not db.is_closed():
            db.close()