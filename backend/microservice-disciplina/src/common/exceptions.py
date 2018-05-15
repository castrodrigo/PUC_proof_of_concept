
class CommonException(Exception):
    def __init__(self, message):
        self.message = message


class JWTRequiredException(CommonException):
    pass


class JWTInvalidException(CommonException):
    pass


class JWTExpiredException(CommonException):
    pass