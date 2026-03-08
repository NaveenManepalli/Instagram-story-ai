import requests

AI_SERVICE_URL = "http://localhost:5001/generate"


def call_ai_service(payload):

    response = requests.post(AI_SERVICE_URL, json=payload)

    return response.json()