#!/bin/sh

set -e
python3 manage.py collectstatic --no-input
python3 manage.py migrate --no-input
exec "$@"
