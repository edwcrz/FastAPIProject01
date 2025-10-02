# from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, WebSocketException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
# import random
from starlette import status

from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1 # minuto
SECRET = "9186f53ac2db04d593302c13305f0bd9975bfd448e30445f327e0bbb2de1f19d"
crypt = CryptContext(schemes=["bcrypt"])

router_instance = APIRouter()

class UserClass(BaseModel):
    username: str
    fullname: str
    email : str
    disabled : bool

class PassClass(UserClass):
    password: str



db = {
        "edwcrz":   {
                    "username": "edwcrz", 
                    "fullname": "Eduardo Cruz", 
                    "email": "edwcrz@gmail.com", 
                    "disabled": False,
                    #"password": "edwcrz123",
                    #"password": crypt.hash("edwcrz123"),
                    "password":"$2a$12$ED3Qh9NiZvQqnuk7mYi6GOxZHh2m4jj4wpL6KM6rPBQG/ANTVk2pW"
                    },
        "cruzeduardoa": {
                        "username": "cruzeduardoa", 
                        "fullname": "Eduardo Cruz", 
                        "email": "cruzeduardoa@gmail.com", 
                        "disabled": False,
                        #"password": "cruzeduardoa123",
                        #"password": crypt.hash("cruzeduardoa123"),
                        "password":"$2a$12$SFAM9CQbumpHuve7e9QupOgbkakQlJGU0Xc/J43eunc9FKLtOpHwm"
                        }
     }

def SearchUserDB(username: str):
    if username in db.keys():
        user_dict = db[username]
        return PassClass(**user_dict)

def SearchTokenDB(token: str):
    user = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    if user:
        user_dict = db.get(user.get("sub"))
        if user_dict:       
            return UserClass(**user_dict)
    return None
    
# print(SearchUserDB("cruzeduardoa"))

oauth = OAuth2PasswordBearer(tokenUrl="login")

@router_instance.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userdedb = db.get(form.username)
    user = SearchUserDB(form.username)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="El usuario no existe")
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Contraseña incorrecta")
    if user.disabled == True:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Usuario inactivo")
    token_expiration = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + token_expiration
    access_token ={
        "sub": user.username,
        "exp": expire,
        "admin": True,
        }
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

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