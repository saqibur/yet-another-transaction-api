from decouple import config

from common.constants import (
    DEVELOPMENT_SERVER,
    LOCAL_SERVER,
    PRODUCTION_SERVER,
    STAGING_SERVER,
)


def restrict_to_development_environment(function):
    def wrapper(*args, **kwargs):
        if config("SERVER_NAME") not in [LOCAL_SERVER, DEVELOPMENT_SERVER]:
            print(
                "Error: Cannot run this command in non-testing environment.",
            )
            return
        return function(*args, **kwargs)

    return wrapper


def restrict_to_non_development_environment(function):
    def wrapper(*args, **kwargs):
        if config("SERVER_NAME") not in [STAGING_SERVER, PRODUCTION_SERVER]:
            print(
                "Error: Cannot run this command in a development environment.",
            )
            return
        return function(*args, **kwargs)

    return wrapper
