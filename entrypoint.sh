#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata data.json
echo "$@"
exec "$@"
