from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = []

@app.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "Usuario creado exitosamente", "user": user}

@app.get("/users/")
def get_users():
    return {"users": users}
