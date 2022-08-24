from typing import Union
from datetime import datetime
import pytz
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hola": "Bienvenid@"}

@app.get('/datetime-host')
async def set_datetime2():
    return {"datetime2": datetime.now()}

@app.get('/datetime-pytz')
async def set_datetime():
    return {"datetime": datetime.now(tz=pytz.timezone('America/Bogota'))}
