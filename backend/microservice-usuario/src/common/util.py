import datetime
import os
import jwt
import re

from passlib.hash import pbkdf2_sha512


class Util(object):

    @staticmethod
    def setup_response_body(message, object=None):
        body = {
            'message': message,
        }
        if object is not None:
            body['payload'] = object
        return body

    @staticmethod
    def hash_password(password):
        """
        :param password: Sha512 from user
        :return: A pbkdf2_sha512 ecrypted from sha512
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        :param password: sha512 hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if matches, False otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile("^[\w-]+@([\w-]+\.)+[\w]+$")
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def encode_jwt_token(name):
        payload = Util.generate_jwt_payload(name)
        return jwt.encode(
            payload,
            os.getenv('JWT_SECRET'),
            algorithm='HS256'
        ).decode('utf-8')

    @staticmethod
    def decode_jwt_token(jwt_key):
        return jwt.decode(
            jwt_key,
            os.getenv('JWT_SECRET'),
            algorithms=['HS256']
        )

    @staticmethod
    def generate_jwt_payload(name):
        return {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(
                seconds=int(os.getenv('JWT_EXPIRE_TIME'))
            ),
            'nbf': datetime.datetime.utcnow(),
            'iss': os.getenv('JWT_ISSUER'),
            'iat': datetime.datetime.utcnow(),
            'name': name
        }