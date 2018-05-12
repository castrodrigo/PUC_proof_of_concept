import os
import pymongo


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
