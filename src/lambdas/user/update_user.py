from src.lambdas.handlers import handle_update_user

def handler(event, context):
    handle_update_user(event, context)
