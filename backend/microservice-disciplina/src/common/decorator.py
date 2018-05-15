import jwt
import os

from flask import jsonify
from flask import Blueprint
from flask import request
from functools import wraps

from src.common.exceptions import JWTRequiredException


class BaseBlueprint(Blueprint):

    def route(self, rule, **options):
        def decorator(f):
            new_rule = rule.rstrip('/')
            new_rule_with_slash = '{}/'.format(new_rule)
            super(BaseBlueprint, self).route(new_rule, **options)(f)
            super(BaseBlueprint, self).route(new_rule_with_slash, **options)(f)
            return f
        return decorator


class AuthCheck(object):

    def check_auth_token(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            try:
                if not request.headers.get("Authorization"):
                    raise JWTRequiredException('Authorization header is missing')
                authorization = request.headers.get("Authorization")

                jwt.decode(authorization, os.getenv('JWT_SECRET'), algorithms=['HS256'])

                return f(*args, **kwargs)
            except JWTRequiredException as e:
                return jsonify({'message': e.message}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Expired token'}), 403
            except Exception:
                return jsonify({'message': 'Invalid token'}), 403

        return decorator
