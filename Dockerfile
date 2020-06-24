FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD deploy/wateringcontrol_nginx.conf /etc/nginx/sites-available/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y nginx vim
RUN ln -s /etc/nginx/sites-available/wateringcontrol_nginx.conf /etc/nginx/sites-enabled/
ADD . /code/
RUN chmod +x entry_point.sh
ENTRYPOINT [ "./entry_point.sh" ]