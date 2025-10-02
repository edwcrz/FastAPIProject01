from fastapi import APIRouter, HTTPException, WebSocketException 
# from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
import random
from starlette import status

router_instance = APIRouter()

class UserClass(BaseModel):
    username: str
    fullname: str
    email : str
    disabled : bool

class PassClass(UserClass):
    password: str
    token: int


db = {
        "edwcrz":   {
                    "username": "edwcrz", 
                    "fullname": "Eduardo Cruz", 
                    "email": "edwcrz@gmail.com", 
                    "disabled": False,
                    "password": "edwcrz123",
                    "token": random.randint(1,10000000)
                    },
        "cruzeduardoa": {
                        "username": "cruzeduardoa", 
                        "fullname": "Eduardo Cruz", 
                        "email": "cruzeduardoa@gmail.com", 
                        "disabled": True,
                        "password": "cruzeduardoa123",
                        "token": random.randint(1,10000000) 
                        }
     }

def SearchUserDB(username: str):
    if username in db.keys():
        user_dict = db[username]
        return PassClass(**user_dict)

def SearchTokenDB(token: str):
    for user_dict in db.values():
        if str(user_dict.get("token")) == str(token):
            return UserClass(**user_dict)
    return None
    
# print(SearchUserDB("cruzeduardoa"))

oauth = OAuth2PasswordBearer(tokenUrl="login")

@router_instance.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userdedb = db.get(form.username)
    if not userdedb:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="El usuario no existe")
    if userdedb.get("password") != form.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Contraseña incorrecta")
    if userdedb.get("disabled"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Usuario inactivo")
    return {"access_token": userdedb.get("token"), "token_type": "bearer"}

@router_instance.get("/users/me")
async def read_users_me(token: str = Depends(oauth)):
    user = SearchTokenDB(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Usuario no encontrado",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    if user.disabled == True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo")

    return user