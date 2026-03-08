from flask_jwt_extended import verify_jwt_in_request
from functools import wraps


def auth_required():

    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()

            return fn(*args, **kwargs)

        return decorator

    return wrapper