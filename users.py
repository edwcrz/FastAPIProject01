from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class user():
    id: int
    name: str
    surname: str
    username: str
    email: str

@app.get("/usersjson")
async def usersjson():
    return [{"id": 1, "name": "Eduardo", "surname": "Cruz", "email": "edwcrz@gmail.com"},
            {"id": 2, "name": "Edw", "surname": "Crz", "email": "edwcrz@gmail.com"},
            {"id": 3, "name": "edw", "surname": "crzdev", "email": "edwcrzdev@gmail.com"}]
