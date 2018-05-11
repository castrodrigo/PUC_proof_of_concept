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