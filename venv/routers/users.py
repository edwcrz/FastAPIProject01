from fastapi import APIRouter, HTTPException, WebSocketException 
from pydantic import BaseModel

router_instance = APIRouter()

@router_instance.get("/users_json")
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

@router_instance.get("/users")
async def get_users():
    return user_list

def search_user (id : int):
    users_list = filter (lambda user_list: user_list.id == id, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'Error al obtener el usuario con id {id}'} 

# por query http
@router_instance.get("/users_query")
async def users_query(id: int):
#    users_list = filter (lambda U: U["id"] == id, user_list)
#    try:
#        return list(users_list)[0]
#    except:
#        return {"error": f'Error al obtener el usuario con id {id} por http query'}
    return search_user(id)

# por path http
@router_instance.get("/user_id/{id}")
async def user_id(id: int):
#    users_list = filter (lambda U: U["id"] == id, user_list)
#    try:
#        return list(users_list)[0]
#    except:
#        return {"error": F'User con id {id} not found'}
    return search_user(id)

@router_instance.get("/user_email/{email}")
async def user_email(email: str):
    users_list = filter (lambda user_list: user_list.email == email, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {email} not found'}

@router_instance.get("/user_name/{name}")
async def user_name(name: str):
    users_list = filter (lambda user_list: user_list.name == name, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {name} not found'}
    
@router_instance.get("/user_surname/{surname}")
async def user_surname(surname: str):
    users_list = filter (lambda user_list: user_list.surname == surname, user_list)
    try:
        return list(users_list)[0]
    except:
        return {"error": f'User con email {surname} not found'}

@router_instance.get("/user_username/{username}")
async def user_username(username: str):
    users_list = filter (lambda user_list: user_list.username == username, user_list)
    try:
        return list(users_list)
    except:
        return {"error": f'User con email {username} not found'}

@router_instance.post("/user_create/", status_code=201)
async def user_create(User_Assigned: User_Class):
    if type (search_user(User_Assigned.id)) == User_Class:
        raise HTTPException(status_code=409, detail=f'User con id {User_Assigned.id} ya existe. No puede ser creado.')
        #return {"error": f'User con id {user.id} ya existe. No puede ser creado.'}
    else:
        user_list.append(User_Assigned)
        return {"message": f'El usuario {User_Assigned.id} fue creado correctamente'}

found= False
@router_instance.put("/user_update/", status_code=202)
async def user_update(User_Updated: User_Class):
    for index, saved_user in enumerate(user_list):
        if saved_user.id == User_Updated.id:
            user_list[index] = User_Updated
            found = True
        else:
            found = False
    if not found:
        raise HTTPException(status_code=412, detail=f'el usuario {User_Updated.id} no existía, debe ser creado previamente mediante el uso de POST, para ser actualizado con PUT')
    else:
        return {"message": f'User con id {User_Updated.id} actualizado correctamente'}


found = False
@router_instance.delete("/user_delete/{id}")
async def user_delete(id: int):
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
        else:
            found = False

    if not found:
        return {"error": f'el usuario {id} que intenta borrar no existía, previamente debe ser creado con POST para ser eliminado con DELETE'}
    else:
        return {"message": f'User con id {id} eliminado correctamente'}
        