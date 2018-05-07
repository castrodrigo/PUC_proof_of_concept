

class SubjectException(Exception):
    def __init__(self, message):
        self.message = message


class SubjectNotFoundException(SubjectException):
    pass