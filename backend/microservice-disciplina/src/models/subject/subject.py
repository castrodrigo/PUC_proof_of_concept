import uuid

from src.common.bootstrap import MongoDB
from src.models.subject.exceptions import SubjectNotFoundException


class Subject(object):
    _collection = 'subjects'

    def __init__(
            self,
            name,
            code,
            summary,
            procedures=None,
            bibliography=None,
            script=None,
            total_hours=None,
            id=None
    ):
        self.id = uuid.uuid4().hex if id is None else id
        self.name = name
        self.code = code
        self.summary = summary
        self.procedures = procedures
        self.bibliography = bibliography
        self.script = script
        self.total_hours = total_hours

    @staticmethod
    def get_subject_by_id(id):
        document = MongoDB.mongo_collection(Subject._collection).find_one(
            {'id': id}, {'_id': False}
        );
        if document is None:
            raise SubjectNotFoundException('Subject not found')
        return document

    @classmethod
    def get_subjects(cls):
        subjects = MongoDB.mongo_collection(Subject._collection).find({}, {'_id': False})
        document_list = [
            cls(**s).json() for s in subjects
        ]
        response = {
            "total": len(document_list),
            "data": document_list
        }
        return response

    def save(self):
        try:
            self.get_subject_by_id(self.id)
            return MongoDB.mongo_collection(self._collection).update(
                {'id': self.id}, self.json()
            )
        except SubjectNotFoundException:
            return MongoDB.mongo_collection(self._collection).insert(self.json())

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'summary': self.summary,
            'procedures': self.procedures,
            'bibliography': self.bibliography,
            'script': self.script,
            'total_hours': self.total_hours
        }

    def __repr__(self):
        return '<Subject {} with name {}, ' \
               'code {}, ' \
               'summary {}, ' \
               'procedures {}, ' \
               'bibliography {}, ' \
               'script {}, ' \
               'total hours {}>'.format(
                    self.id,
                    self.name,
                    self.code,
                    self.summary,
                    self.procedures,
                    self.bibliography,
                    self.script,
                    self.total_hours
                )

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "code": {"type": "string"},
            "summary": {"type": "string"},
            "procedures": {"type": "string"},
            "bibliography": {"type": "string"},
            "script": {"type": "string"},
            "total_hours": {"type": "integer"}
        },
        "required": ["name", "code", "summary"]
    }