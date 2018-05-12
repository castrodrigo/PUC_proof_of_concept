import os
import pymongo

from flask import Blueprint

class MongoDB(object):
    client = None
    _connection_string = os.getenv('MONGO_CONNECTION_STRING')
    _database = os.getenv('MONGO_DB_NAME')

    @classmethod
    def _connect(cls):
        cls.client = pymongo.MongoClient(cls._connection_string)

    @classmethod
    def mongo_collection(cls, collection):
        if cls.client is None:
            cls._connect()
        return cls.client[cls._database][collection]


class BaseBlueprint(Blueprint):

    def route(self, rule, **options):
        def decorator(f):
            new_rule = rule.rstrip('/')
            new_rule_with_slash = '{}/'.format(new_rule)
            super(BaseBlueprint, self).route(new_rule, **options)(f)
            super(BaseBlueprint, self).route(new_rule_with_slash, **options)(f)
            return f
        return decorator