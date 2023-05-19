from pydantic import BaseModel

class UserSchema(BaseModel):
    user_id: str
    username: str
    email: str
    password: str
