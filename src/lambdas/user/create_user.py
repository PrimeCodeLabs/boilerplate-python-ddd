from src.lambdas.handlers import handle_create_user

def handler(event, context):
    handle_create_user(event, context)
