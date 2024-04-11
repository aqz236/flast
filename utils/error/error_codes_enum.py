from enum import Enum


class ErrorCode(Enum):
    UNEXPECTED_ERROR = 'Unexpected error occurred, please try again later.', 500
    INVALID_VALUE = 'Invalid value provided.', 400
    WRONG_TYPE = 'Wrong type provided.', 400
