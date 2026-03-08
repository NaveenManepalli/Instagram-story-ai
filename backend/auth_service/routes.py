from flask import Blueprint, request, jsonify
from auth_service.service import login_user, signup_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    result = signup_user(data)
    return jsonify(result)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    result = login_user(data)
    return jsonify(result)