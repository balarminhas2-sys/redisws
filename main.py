from typing import Optional
import redis
from fastapi import FastAPI

app = FastAPI()


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
    r.set("Temperature", "30")
    r.set("Humidity", "21")
    data = r.get(key).decode()
    return {"key_name":key, "value":data}