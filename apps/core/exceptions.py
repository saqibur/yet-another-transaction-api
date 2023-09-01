# Standard library imports
from sys import stdout
import traceback

# Django imports
from django.http import Http404
from rest_framework.exceptions import (
    ValidationError,
    NotFound,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler

# Third party imports
from decouple import config

# Local imports
from common.constants import LOCAL_SERVER


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Http404):
        exc = NotFound(exc.__str__())

    if response is None:
        stdout.write(traceback.format_exc())
        if config("SERVER_NAME") == LOCAL_SERVER:
            return response
        return Response(
            {
                "success": False,
                "code": HTTP_500_INTERNAL_SERVER_ERROR,
                "type": "non_field_error",
                "error_message": "Unhandled exception",
                "details": {
                    "exception": type(exc).__name__,
                    "message": str(exc),
                    "code": "unhandled_exception",
                },
            },
            status=HTTP_500_INTERNAL_SERVER_ERROR,
        )

    details = []
    if isinstance(exc, ValidationError):
        errors = response.data
        error_type = "field_error"

        if isinstance(errors, dict):
            for field, field_errors in errors.items():
                details.append(
                    {
                        "field": field,
                        "errors": [str(error) for error in field_errors],
                    }
                )
        elif isinstance(errors, list):
            for error in errors:
                details.append(
                    {
                        "field": error.code,
                        "errors": [str(error)],
                    }
                )
    else:
        error = response.data
        error_type = "non_field_error"

        details = {
            "exception": type(exc).__name__,
            "message": str(error["detail"]),
            "code": error["detail"].code,
        }

        if config("SERVER_NAME") == LOCAL_SERVER:
            details.update({"traceback": traceback.format_exc()})
        else:
            stdout.write(traceback.format_exc())

    error_payload = {
        "success": False,
        "code": response.status_code,
        "type": error_type,
        "error_message": exc.default_detail,
        "details": details,
    }

    response.data = error_payload
    return response
