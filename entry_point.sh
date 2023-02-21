#!/bin/sh

if [ "${ENVIRONMENT}" == "local" ]; then
    cd /host/code && python manage.py runserver 0.0.0.0:8001 &
    cd /code
fi

gunicorn watering_control.wsgi --bind 0.0.0.0:8000
