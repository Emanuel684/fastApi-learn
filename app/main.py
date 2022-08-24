from typing import Union
from datetime import datetime
import pytz

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    print("read_item: ", item_id)
    print("q read_item: ", q)
    return {"item_id": item_id, "q": q}

@app.get('/users/{user_id}')
async def read_user(user_id: int):
    return {"user_id": user_id}

# docker run -d --name contfastapi -p 80:80 -v /etc/localtime:/etc/localtime:ro fastapi
@app.get('/datetime2')
async def set_datetime2():
    return {"datetime2": datetime.now()}

@app.get('/datetime')
async def set_datetime():
    return {"datetime": datetime.now(tz=pytz.timezone('America/Bogota'))}
