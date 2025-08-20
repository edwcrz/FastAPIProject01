from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel

fastapi_Instance = FastAPI()

# class User(BaseModel):
#    name: str
#    surname: str
#    mail: str
#    age = int

# Users = User("Eduardo", "Cruz", "edwcrz@gmail.com", 35)

# @app.get("/userclass")
# async def userclass():
#     return Users(name = "Edu", surname = "Crz", mail = "edwcrz@gmail.com", age = 33)
@fastapi_Instance.get("/")
async def root():
    return  {"Hello" : "World FastAPI", 
             "Mail" : "edwcrz@gmail.com", 
             "Age" : 35
            }

@fastapi_Instance.get("/cv")
async def get_cv():
    return  {"Name" : "Eduardo Cruz", 
             "Mail" : "cruzeduardoa@gmail.com", 
             "Age" : 49
            }