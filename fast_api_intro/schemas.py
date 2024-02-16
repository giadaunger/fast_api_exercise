from pydantic import BaseModel, Field, field_validator

class UserSchema(BaseModel):
    id: int = Field(gt=0, lte=100000000000000)
    name: str = Field(min_length=1)
    email: str | None = Field(default=None, max_length=20, min_length=5)
    is_active: bool