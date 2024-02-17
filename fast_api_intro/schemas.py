from pydantic import BaseModel, Field, field_validator
    
class ProfileSchema(BaseModel):
    bio: str = Field(max_length=2000)
    age: int = Field(gt=0, lt=500)
    
class PostSchema(BaseModel):
    id: int = Field(gt=0)
    title: str
    content: str

class UserSchema(BaseModel):
    id: int = Field(gt=0, lt=10000000000)
    name: str = Field(min_length=1)
    is_active: bool
    email: str | None = Field(default=None, max_length=20, min_length=5)

class UserPostsSchema(BaseModel):
    id: int = Field(gt=0, lt=10000000000)
    name: str = Field(min_length=1)
    is_active: bool
    email: str | None = Field(default=None, max_length=20, min_length=5)
    profile: ProfileSchema
    posts: list[PostSchema]
    
    @field_validator("name")
    def validate_name(cls, name: str) -> str:
        print(name)
        if name == "crap":
            raise ValueError("Error: Bad language")
        return name