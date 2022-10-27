from fastapi import FastAPI

app = FastAPI() #instanciar la clase

@app.get('/')

def home():
    return {
        "hola" : "Estudiante"
    }