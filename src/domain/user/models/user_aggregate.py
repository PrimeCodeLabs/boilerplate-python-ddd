from dataclasses import dataclass
from src.domain.user.models.user import User

@dataclass
class UserAggregate:
    user: User
    # Other related entities or value objects can be included here
