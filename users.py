from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/users")
async def users():
    return [{"id": 1, "name": "Eduardo", "surname": "Cruz", "email": "edwcrz@gmail.com"},
            {"id": 2, "name": "Edw", "surname": "Crz", "email": "edwcrz@gmail.com"},
            {"id": 3, "name": "edw", "surname": "crzdev", "email": "edwcrzdev@gmail.com"}]
