from flask import Blueprint
from flask import request
from flask import jsonify

from jsonschema import exceptions as jsonschema_exceptions
from jsonschema import validate

from src.common.util import Util
from src.models.course.course import Course
from src.models.course.exceptions import CourseNotFoundException

course_blueprint = Blueprint('courses', __name__)


@course_blueprint.route('/<string:id>', methods=['GET'])
def get_course(id):
    try:
        document = Course.get_course_by_id(id)
        return jsonify(document), 200
    except CourseNotFoundException as e:
        return jsonify(Util.setup_response_body(e.message)), 404


@course_blueprint.route('/<string:id>', methods=['PUT'])
def put_course(id):
    try:
        payload = request.get_json()
        validate(payload, Course.schema)

        payload['script'] = None if 'script' not in payload else payload['script']
        payload['id'] = id

        course = Course(**payload)
        course.save()

        return jsonify(), 204
    except jsonschema_exceptions.ValidationError as e:
        return jsonify(Util.setup_response_body(e.message)), 422


@course_blueprint.route('/', methods=['GET'])
def get_courses():
    try:
        response = Course.get_courses()
        return jsonify(response), 200
    except Exception:
        return jsonify(Util.setup_response_body('Operation not completed')), 500


@course_blueprint.route('/', methods=['POST'])
def post_course():
    try:
        payload = request.get_json()
        validate(payload, Course.schema)

        payload['script'] = None if 'script' not in payload else payload['script']

        course = Course(**payload)
        course.save()

        return jsonify(), 204
    except jsonschema_exceptions.ValidationError as e:
        return jsonify(Util.setup_response_body(e.message)), 422
