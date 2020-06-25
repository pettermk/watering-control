#!/bin/bash
cp /host/etc/ssl/certs/nginx-selfsigned.crt /etc/ssl/certs/
cp /host/etc/ssl/private/nginx-selfsigned.key /etc/ssl/private/
cp /host/etc/nginx/dhparam.pem /etc/nginx
uwsgi --ini /code/deploy/wateringcontrol_uwsgi.ini &
python manage.py runserver 0.0.0.0:8001 &
nginx -g 'daemon off;'
