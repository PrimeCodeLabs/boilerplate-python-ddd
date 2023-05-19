from dataclasses import dataclass

@dataclass
class User:
    user_id: str
    username: str
    email: str
    password: str
    # Other user properties and methods can be added here
