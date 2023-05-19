from src.infrastructure.events.eventbridge import EventBridge

class EventBridgeAdapter:
    def __init__(self):
        self.event_bridge = EventBridge()  # Initialize the EventBridge integration

    def publish_event(self, event: dict):
        self.event_bridge.publish(event)  # Publish event using the EventBridge integration
