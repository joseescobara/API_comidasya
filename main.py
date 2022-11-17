#aquí vamos a correr nuestra api

from fastapi import FastAPI

from app.v1.router.user_router import router as user_router

app = FastAPI() #instanciar la clase


app.include_router(user_router)