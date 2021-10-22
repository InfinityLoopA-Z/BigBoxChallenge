#!/bin/bash
python manage.py collectstatic --noimput
python manage.py migrate
echo "$@"
exec "$@"
