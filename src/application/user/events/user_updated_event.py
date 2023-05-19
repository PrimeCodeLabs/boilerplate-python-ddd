from dataclasses import dataclass

@dataclass
class UserUpdatedEvent:
    user_id: str
    username: str
    email: str
