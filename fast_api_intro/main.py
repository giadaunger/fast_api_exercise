from fastapi import FastAPI, HTTPException
from schemas import UserSchema, UserPostsSchema

data = {
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "is_active": True,
      "profile": {"age": 30, "bio": "Blablabla"},
      "posts": [
        {
          "id": 1,
          "title": "John's First Post",
          "content": "This is the content of John's first post."
        },
        {
          "id": 2,
          "title": "John's Second Post",
          "content": "This is the content of John's second post."
        }
      ]
    },
    {
      "id": 2,
      "name": "Jane Doe",
      "email": "jane.doe@example.com", # fix
      "is_active": False,
      "profile": {"age": 35, "bio": "sadsadsadsaBlablabla"},# fix
      "posts": [
        {
          "id": 1,
          "title": "Jane's First Post",
          "content": "This is the content of Jane's first post."
        }
      ] #fix
    }
  ]
}

app = FastAPI()

@app.get("/", tags=["status"])
def get_status():
    return {"message": "OK!!!!"}

@app.get("/users", tags=["users"])
def get_users():
    return data["users"]

@app.get("/users/list", tags=["users"])
def get_users_limit(limit: int | None = None):
    if limit is not None:
        return data["users"][:limit]
    return data["users"]

@app.get("/users/{id}", tags=["users"])
def get_user_detail(id: int, name: str):
    print(name)
    for user in data["users"]:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
    
@app.post("/users", tags=["users"])
def add_user(user: UserSchema):
    data["users"].append(user.model_dump())
    return user

@app.post("/posts/users", tags=["users"])
def add_user(user: UserPostsSchema):
    data["users"].append(user.model_dump())
    return user