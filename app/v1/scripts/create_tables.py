from app.v1.model.user_model import User
from app.v1.model.domicilios_model import Domicilio
from app.v1.model.empleados_model import Empleados
from app.v1.model.menu_model import Menu
from app.v1.model.sucursales_model import Sucursales
from app.v1.model.ventas_model import Ventas


from app.v1.utils.db import db

def create_tables():
    """Crea las tablas para los modelos User, Domicilio, Empleados, Menu, Sucursales, Ventas.
    """
    with db:
        db.create_tables([User, Domicilio, Empleados, Menu, Sucursales, Ventas])

