import uuid

from src.common.bootstrap import MongoDB
from src.models.course.exceptions import CourseNotFoundException


class Course(object):
    _collection = 'courses'

    def __init__(
            self,
            name,
            code,
            type,
            subjects,
            semesters,
            summary,
            script=None,
            id=None
    ):
        self.id = uuid.uuid4().hex if id is None else id
        self.name = name
        self.code = code
        self.type = type
        self.subjects = subjects
        self.semesters = semesters
        self.summary = summary
        self.script = script

    @staticmethod
    def get_course_by_id(id):
        document = MongoDB.mongo_collection(Course._collection).find_one(
            {'id': id}, {'_id': False}
        );
        if document is None:
            raise CourseNotFoundException('Course not found')
        return document

    @classmethod
    def get_courses(cls):
        courses = MongoDB.mongo_collection(Course._collection).find({}, {'_id': False})
        document_list = [
            cls(**s).json() for s in courses
        ]
        response = {
            "total": len(document_list),
            "data": document_list
        }
        return response

    def save(self):
        try:
            self.get_course_by_id(self.id)
            return MongoDB.mongo_collection(self._collection).update(
                {'id': self.id}, self.json()
            )
        except CourseNotFoundException:
            return MongoDB.mongo_collection(self._collection).insert(self.json())

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'type': self.type,
            'subjects': self.subjects,
            'semesters': self.semesters,
            'summary': self.summary,
            'script': self.script
        }

    def __repr__(self):
        return '<course {} with name {}, ' \
               'code {}, ' \
               'type {}, ' \
               'subjects {}, ' \
               'semesters {}, ' \
               'script {}, ' \
               'total hours {}>'.format(
                    self.id,
                    self.name,
                    self.code,
                    self.type,
                    self.subjects,
                    self.semesters,
                    self.summary,
                    self.script
                )

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "code": {"type": "string"},
            "type": {"type": "string"},
            "subjects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "semester": {"type": "integer"}
                    }
                }
            },
            "semesters": {"type": "integer"},
            "summary": {"type": "string"},
            "script": {"type": "string"}
        },
        "required": ["name", "code", "type", "subjects", "semesters", "summary"]
    }