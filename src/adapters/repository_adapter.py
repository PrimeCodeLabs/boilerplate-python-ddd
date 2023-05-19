from src.infrastructure.repository.user_repository_impl import UserRepositoryImpl
from src.domain.user.repositories.user_repository_interface import UserRepositoryInterface

class UserRepositoryAdapter:
    def __init__(self):
        self.user_repository = UserRepositoryImpl()  # Initialize the user repository implementation

    def create_user(self, username: str, email: str, password: str) -> str:
        return self.user_repository.create_user(username, email, password)  # Call the repository method

    def update_user(self, user_id: str, username: str, email: str, password: str):
        self.user_repository.update_user(user_id, username, email, password)  # Call the repository method

    def get_user_by_id(self, user_id: str):
        return self.user_repository.get_user_by_id(user_id)  # Call the repository method
