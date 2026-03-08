from app_service.ai_client.ai_client import call_ai_service


def generate_story(payload):

    response = call_ai_service(payload)

    return response