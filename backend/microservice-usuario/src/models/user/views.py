from flask import Blueprint
from flask import request
from flask import jsonify

from jsonschema import exceptions as jsonschema_exceptions
from jsonschema import validate

from src.common.util import Util
from src.models.user.user import User
from src.models.user.exceptions import UserNotFoundException

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/<string:id>', methods=['GET'])
def get_user(id):
    try:
        document = User.get_user_by_id(id)
        return jsonify(document), 200
    except UserNotFoundException as e:
        return jsonify(Util.setup_response_body(e.message)), 404


@user_blueprint.route('/', methods=['GET'])
def get_users():
    try:
        response = User.get_users()
        return jsonify(response), 200
    except Exception:
        return jsonify(Util.setup_response_body('Operation not completed')), 500


@user_blueprint.route('/', methods=['POST'])
def post_user():
    try:
        payload = request.get_json()
        validate(payload, User.schema)

        user = User(**payload)
        user.save()

        return jsonify(), 204
    except jsonschema_exceptions.ValidationError as e:
        return jsonify(Util.setup_response_body(e.message)), 422
