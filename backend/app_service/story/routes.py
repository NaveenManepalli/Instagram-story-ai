from flask import Blueprint, request, jsonify
from middleware.auth_guard import auth_required
from app_service.story.service import generate_story

story_bp = Blueprint("story", __name__)

@story_bp.route("/generate", methods=["POST"])
@auth_required()
def generate():

    payload = request.json

    result = generate_story(payload)

    return jsonify(result)