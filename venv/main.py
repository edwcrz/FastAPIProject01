from fastapi import FastAPI
from pydantic import BaseModel
from routers import products, users, jwt01, auth01

fastapi_instance = FastAPI()

@fastapi_instance.get("/")
async def root():
    return  {"Hello" : "World FastAPI", 
             "Mail" : "edwcrz@gmail.com", 
             "Age" : 35
            }

@fastapi_instance.get("/cv")
async def get_cv():
    return  {"Name" : "Eduardo Cruz", 
             "Mail" : "cruzeduardoa@gmail.com", 
             "Age" : 49
            }

# routers
fastapi_instance.include_router(products.router_instance)
fastapi_instance.include_router(users.router_instance)
# fastapi_instance.include_router(auth01.router_instance)
fastapi_instance.include_router(jwt01.router_instance)