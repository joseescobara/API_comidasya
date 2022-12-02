#aquí vamos a correr nuestra api

from fastapi import FastAPI

from app.v1.router.user_router import router as user_router
from app.v1.router.empleados_router import router as empleados_router
from app.v1.router.sucursales_router import router as sucursales_router
from app.v1.router.menus_router import router as menu_router
from app.v1.router.ventas_router import router as ventas_router
from app.v1.router.domicilios_router import router as domicilios_router

app = FastAPI() 


app.include_router(user_router)
app.include_router(empleados_router)
app.include_router(sucursales_router)
app.include_router(menu_router)
app.include_router(ventas_router)
app.include_router(domicilios_router)
