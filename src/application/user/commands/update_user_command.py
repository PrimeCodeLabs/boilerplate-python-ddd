from dataclasses import dataclass

@dataclass
class UpdateUserCommand:
    user_id: str
    username: str
    email: str
    password: str
