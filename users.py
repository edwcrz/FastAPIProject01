from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/users_json")
async def users_json():
    return user_list_json

user_list_json = [
    {"id": 1, "name": "Eduardo", "surname": "Cruz", "username" : "edulamugre", "email": "cruzeduardoa@gmail.com"},
    {"id": 2, "name": "edu", "surname": "crz", "username" : "edulamugre", "email": "edwcrz@gmail.com"},
    {"id": 3, "name": "edw", "surname": "crzdev", "username" : "edulamugre", "email": "edwcrzdev@gmail.om"}
]

class User_Class(BaseModel):
    id: int
    name: str
    surname: str
    username: str
    email: str

# Usuario = User_Class(id= 0, name="", surname="", username="", email="")

user_list = [User_Class(id= 1, name= "Eduardo", surname= "Cruz", username= "cruze", email= "cruzedu@gmail.com"),
             User_Class(id= 2, name= "edw", surname= "crz", username= "edwcrz", email= "edwcrz@gmail.com"),
             User_Class(id= 3, name= "edu", surname= "crzdev", username= "educrz", email= "edwcrzdev@gmail.com")]


def search_user (id : int):
    users_list = filter (lambda user_list: user_list.id == id, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'Error al obtener el usuario con id {id}'} 

# por query http
@app.get("/users_query")
async def users_query(id: int):
#    users_list = filter (lambda U: U["id"] == id, user_list)
#    try:
#        return list(users_list)[0]
#    except:
#        return {"error": f'Error al obtener el usuario con id {id} por http query'}
    return search_user(id)

# por path http
@app.get("/user_id/{id}")
async def user_id(id: int):
#    users_list = filter (lambda U: U["id"] == id, user_list)
#    try:
#        return list(users_list)[0]
#    except:
#        return {"error": F'User con id {id} not found'}
    return search_user(id)

@app.get("/user_email/{email}")
async def user_email(email: str):
    users_list = filter (lambda user_list: user_list.email == email, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {email} not found'}

@app.get("/user_name/{name}")
async def user_name(name: str):
    users_list = filter (lambda user_list: user_list.name == name, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {name} not found'}
    
@app.get("/user_surname/{surname}")
async def user_surname(surname: str):
    users_list = filter (lambda user_list: user_list.surname == surname, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {surname} not found'}

@app.get("/user_username/{username}")
async def user_username(username: str):
    users_list = filter (lambda user_list: user_list.username == username, user_list)
    try:
        return list(users_list)
    except:
        return {"error": f'User con email {username} not found'}

@app.post("/user_create/")
async def user_create(user: User_Class):
    if type (search_user(user.id)) == User_Class:
        return {"error": f'User con id {user.id} ya existe'}
    else:
        user_list.append(user)
        return {"message": "User created successfully", "user": user} 
