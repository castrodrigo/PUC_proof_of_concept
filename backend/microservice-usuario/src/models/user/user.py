import datetime
import uuid

from src.common.bootstrap import MongoDB
from src.common.util import Util
from src.models.user.exceptions import UserIncorrectPasswordException
from src.models.user.exceptions import UserNotFoundException


class User(object):
    _collection = 'users'

    def __init__(
            self,
            name,
            username,
            email,
            password,
            type,
            id=None,
            created_at=None,
            updated_at=None,
    ):
        self.id = uuid.uuid4().hex if id is None else id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.type = type
        self.updated_at = str(datetime.datetime.now(datetime.timezone.utc)) \
            if updated_at is None else updated_at
        self.created_at = self.updated_at \
            if created_at is None else created_at

    @classmethod
    def is_login_valid(cls, username, password):
        user_data = cls.get_user_by_username(username)
        if user_data is None:
            raise UserNotFoundException("Invalid user")
        if not Util.check_hashed_password(password, user_data['password']):
            raise UserIncorrectPasswordException("Invalid password")
        return True

    @staticmethod
    def get_user_by_id(id):
        document = MongoDB.mongo_collection(User._collection).find_one(
            {'id': id}, {'_id': False}
        )
        if document is None:
            raise UserNotFoundException('User not found')
        return document

    @staticmethod
    def get_user_by_username(username):
        document = MongoDB.mongo_collection(User._collection).find_one(
            {'username': username}, {'_id': False}
        )
        if document is None:
            raise UserNotFoundException('User not found')
        return document

    @classmethod
    def get_users(cls):
        users = MongoDB.mongo_collection(User._collection).find({}, {'_id': False})
        document_list = [
            cls(**s).json(safe=True) for s in users
        ]
        response = {
            "total": len(document_list),
            "data": document_list
        }
        return response

    def save(self):
        try:
            document = self.get_user_by_id(self.id)
            if 'created_at' in document:
                self.created_at = document['created_at']

            return MongoDB.mongo_collection(self._collection).update(
                {'id': self.id}, self.json()
            )
        except UserNotFoundException:
            return MongoDB.mongo_collection(self._collection).insert(self.json())

    def json(self, safe=False):
        json = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'type': self.type,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        if safe:
            del json['password']
        return json

    def __repr__(self):
        return '<User {} with username {}, ' \
               'name {}, ' \
               'email {}, ' \
               'type {}, ' \
               'created at {}' \
               'updated at {}>'.format(
                    self.id,
                    self.username,
                    self.name,
                    self.email,
                    self.type,
                    self.created_at,
                    self.updated_at
                )

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "type": {"type": "string"},
            "password": {"type": "string"},
        },
        "required": ["name", "username", "email", "password", "type"]
    }