from pydantic import BaseModel

class UpdateUserSchema(BaseModel):
    username: str
    email: str
    password: str
