from application.user.commands.create_user_command import CreateUserCommand
from application.user.commands.update_user_command import UpdateUserCommand
from application.user.events.user_created_event import UserCreatedEvent
from application.user.events.user_updated_event import UserUpdatedEvent
from src.adapters.eventbridge_adapter import EventBridgeAdapter
from src.adapters.repository_adapter import UserRepositoryAdapter

class UserService:
    def __init__(self):
        self.user_repository = UserRepositoryAdapter()
        self.event_bridge = EventBridgeAdapter()

    def create_user(self, command: CreateUserCommand) -> UserCreatedEvent:
        # Business logic to create a user
        # ...

        # Save user to repository
        user_id = self.user_repository.create_user(command.username, command.email, command.password)

        # Emit user created event
        event = UserCreatedEvent(user_id=user_id, username=command.username, email=command.email)
        self.event_bridge.publish_event(event)  # Publish event using the EventBridge adapter

        return event

    def update_user(self, command: UpdateUserCommand) -> UserUpdatedEvent:
        # Business logic to update a user
        # ...

        # Update user in repository
        self.user_repository.update_user(command.user_id, command.username, command.email, command.password)

        # Emit user updated event
        event = UserUpdatedEvent(user_id=command.user_id, username=command.username, email=command.email)
        self.event_bridge.publish_event(event)  # Publish event using the EventBridge adapter

        return event
