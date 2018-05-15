from flask import request
from flask import jsonify

from jsonschema import exceptions as jsonschema_exceptions
from jsonschema import validate

from src.common.util import Util
from src.common.decorator import BaseBlueprint
from src.common.decorator import AuthCheck as auth_decorator

from src.models.user.user import User
from src.models.user.exceptions import UserIncorrectPasswordException
from src.models.user.exceptions import UserNotFoundException


user_blueprint = BaseBlueprint('users', __name__)


@user_blueprint.route('/authenticate', methods=['POST'])
def authenticate():
    try:
        headers = {}
        if "username" in request.headers:
            headers['username'] = request.headers['username']
        if "password" in request.headers:
            headers['password'] = request.headers['password']
        validate(headers, User.headers_schema)

        user = User.get_user_by_username(headers['username'])
        if not Util.check_hashed_password(headers['password'], user.password):
            raise UserIncorrectPasswordException("Invalid Password")

        response = {
            'jwt_token': Util.encode_jwt_token(headers['username'])
        }
        return jsonify(response), 200
    except jsonschema_exceptions.ValidationError as e:
        return jsonify(Util.setup_response_body("Headers: {}".format(e.message))), 403
    except UserIncorrectPasswordException as e:
        return jsonify(Util.setup_response_body(e.message)), 403
    except UserNotFoundException as e:
        return jsonify(Util.setup_response_body(e.message)), 404


@user_blueprint.route('/<string:id>', methods=['GET'])
@auth_decorator.check_auth_token
def get_user(id):
    try:
        user = User.get_user_by_id(id)
        return jsonify(user.json(safe=True)), 200
    except UserNotFoundException as e:
        return jsonify(Util.setup_response_body(e.message)), 404


@user_blueprint.route('/', methods=['GET'])
@auth_decorator.check_auth_token
def get_users():
    try:
        response = User.get_users()
        return jsonify(response), 200
    except Exception:
        return jsonify(Util.setup_response_body('Operation not completed')), 500


@user_blueprint.route('/', methods=['POST'])
@auth_decorator.check_auth_token
def post_user():
    try:
        payload = request.get_json()
        validate(payload, User.schema)

        user = User(**payload)
        user.save()

        return jsonify(), 204
    except jsonschema_exceptions.ValidationError as e:
        return jsonify(Util.setup_response_body(e.message)), 422
