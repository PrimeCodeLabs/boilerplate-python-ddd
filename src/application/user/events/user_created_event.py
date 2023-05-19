from dataclasses import dataclass

@dataclass
class UserCreatedEvent:
    user_id: str
    username: str
    email: str
