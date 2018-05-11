

class UserException(Exception):
    def __init__(self, message):
        self.message = message


class UserNotFoundException(UserException):
    pass


class UserIncorrectPasswordException(UserException):
    pass


class UserAlreadyRegisteredException(UserException):
    pass


class UserInvalidEmailException(UserException):
    pass