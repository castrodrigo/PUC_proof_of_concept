

class CourseException(Exception):
    def __init__(self, message):
        self.message = message


class CourseNotFoundException(CourseException):
    pass