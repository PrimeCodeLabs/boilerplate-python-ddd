from abc import ABC, abstractmethod
from src.domain.user.models.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> str:
        pass

    @abstractmethod
    def update_user(self, user_id: str, username: str, email: str, password: str):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User:
        pass

    # Other repository methods can be added here
