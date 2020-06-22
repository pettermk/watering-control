FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD deploy/wateringcontrol_nginx.conf /etc/nginx/sites-available/
RUN pip install -r requirements.txt
RUN apt update && apt install nginx
ADD . /code/
RUN chmod +x entry_point.sh
CMD [ "./entry_point.sh" ]