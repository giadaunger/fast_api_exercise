from fastapi import FastAPI
from schemas import UserSchema

data = {
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "is_active": True
    },
    {
      "id": 2,
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "is_active": False
    }
  ]
}

app = FastAPI()

@app.get("/", tags=["status"])
def get_status():
    return {"message": "OK"}

@app.get("/users", tags=["users"])
def get_users():
    return data["users"]

@app.get("/users/{id}", tags=["users"])
def get_user_details(id: int):
    return {}

@app.get("/users/list", tags=["users"])
def get_users(limit: int):
    if limit is not None:
        return data["users"][:limit]
    return data["users"]

@app.post("/users", tags=["users"])
def add_user(user: UserSchema):
    data["users"].append(user.model_dump())
    return user