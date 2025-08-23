from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    username: str
    email: str

@app.get("/users_class")
async def users_class():
    try:
        return User(id= 11 , name= "José", surname= "Chilavert", username= "chila", email= "chilavert@gmail.com")
    except:
        return {"error": f'Error al obtener el usuario'} 

user_list = [{"id": 1, "name": "Eduardo", "surname": "Cruz", "username" : "edulamugre", "email": "cruzeduardoa@gmail.com"},
             {"id": 2, "name": "edu", "surname": "crz", "username" : "edulamugre", "email": "edwcrz@gmail.com"},
             {"id": 3, "name": "edw", "surname": "crzdev", "username" : "edulamugre", "email": "edwcrzdev@gmail.com"}]

@app.get("/users_json")
async def users_json():
    return user_list

@app.get("/user_id/{id}")
async def user_id(id: int):
    users_list = filter (lambda U: U["id"] == id, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": F'User con id {id} not found'}


@app.get("/user_email/{email}")
async def user_email(email: str):
    users_list = filter (lambda U: U["email"] == email, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {email} not found'}

@app.get("/user_name/{name}")
async def user_name(name: str):
    users_list = filter (lambda U: U["name"] == name, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {name} not found'}
    
@app.get("/user_surname/{surname}")
async def user_surname(surname: str):
    users_list = filter (lambda U: U["surname"] == surname, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {surname} not found'}

@app.get("/user_username/{username}")
async def user_username(username: str):
    users_list = filter (lambda U: U["username"] == username, user_list)
    try:
        return list(users_list)
    except:
        return {"error": f'User con email {username} not found'}