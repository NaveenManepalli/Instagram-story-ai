from auth_service.models import User
from utils.password import hash_password, verify_password
from utils.jwt_handler import generate_token
from database.db import db


def signup_user(data):

    user = User(
        email=data["email"],
        password=hash_password(data["password"])
    )

    db.session.add(user)
    db.session.commit()

    token = generate_token(user.id)

    return {"token": token}


def login_user(data):

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return {"error": "user not found"}

    if not verify_password(data["password"], user.password):
        return {"error": "invalid password"}

    token = generate_token(user.id)

    return {"token": token}