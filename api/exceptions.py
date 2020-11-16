from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class MissingParamsException(APIException):

    status_code = 400  # Bad request.
    default_detail = 'Some required parameters are missing. Check your request.'
    default_code = 'missing_params'


class WrongParamsException(APIException):

    status_code = 400  # Bad request.
    default_detail = 'Some parameters were sent with an unacceptable value. Check your request.'
    default_code = 'wrong_params'


class CalculationErrorException(APIException):

    status_code = 500  # Internal server error.
    default_detail = 'There was an error while calculating your data.'
    default_code = 'calculation_error'
