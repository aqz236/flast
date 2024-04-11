from flask import jsonify, current_app
from functools import wraps
from .error_codes_enum import ErrorCode
from .status_codes_enum import StatusCode

def handle_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as ve:
            current_app.logger.error('ValueError: %s', ve)
            return jsonify({'status': 'error', 'message': ErrorCode.INVALID_VALUE.value[0]}), StatusCode.BAD_REQUEST.value

        except TypeError as te:
            current_app.logger.error('TypeError: %s', te)
            return jsonify({'status': 'error', 'message': ErrorCode.WRONG_TYPE.value[0]}), StatusCode.BAD_REQUEST.value

        except Exception as e:
            current_app.logger.error('Unexpected error: %s', e)
            return jsonify({'status': 'error', 'message': ErrorCode.UNEXPECTED_ERROR.value[0]}), StatusCode.INTERNAL_SERVER_ERROR.value
    return decorated_function