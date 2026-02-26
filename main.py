from typing import Optional
import redis
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
r = redis.from_url("rediss://red-d566ok95pdvs73ch3qkg:vFJ6IyTkoE8TUCnwnWLwc9BvEznPaLDU@ohio-keyvalue.render.com:6379")

class weather_data(BaseModel):
    temperature: float | None = None
    humidity: float | None = None


class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/name")
async def name():
    return {"name":"Balar"}

@app.get("/names/{myname}")
async def names(myname:str):
    return {"name":f"your name is {myname}"}



@app.get("/redis/{key}")
async def getdata(key:str):
    r = redis.from_url("rediss://red-d566ok95pdvs73ch3qkg:vFJ6IyTkoE8TUCnwnWLwc9BvEznPaLDU@ohio-keyvalue.render.com:6379")
    data = r.get(key).decode()
    return {"key_name":key, "value":data}

@app.post("/weather_data")
async def create_item(item: weather_data):
    print(item.temperature)
    print(item.humidity)
    r.set("Temperature", str(item.temperature))
    r.set("Humidity", str(item.humidity))
    return item

@app.post("/weather_data/temperature")
async def create_temperature(item: weather_data):
    print(item.temperature)
    r.set("Temperature", str(item.temperature))
    return item

@app.post("/weather_data/humidity")
async def create_humidity(item: weather_data):
    print(item.humidity)
    r.set("Humidity", str(item.humidity))
    return item
