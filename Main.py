from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    mail: str
    age = int

Users = User("Eduardo", "Cruz", "edwcrz@gmail.com", 35)

@app.get("/userclass")
async def userclass():
    return Users(name = "Edu", surname = "Crz", mail = "edwcrz@gmail.com", age = 33)

# @app.get("/cv")
# async def read_root():
#    return  {"Name" : "Eduardo Cruz"}

