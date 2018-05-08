

class Util(object):

    @staticmethod
    def setup_response_body(message, object=None):
        body = {
            'message': message,
        }
        if object is not None:
            body['payload'] = object
        return body