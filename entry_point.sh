#!/bin/bash
python manage.py collectstatic &
uwsgi --ini /code/deploy/wateringcontrol_uwsgi.ini &
python manage.py runserver 0.0.0.0:8001 &
nginx -g 'daemon off;'
