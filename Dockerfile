FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -sL 'https://getenvoy.io/gpg' | apt-key add -
# verify the key
RUN apt-key fingerprint 6FF974DB | grep "5270 CEAC"
RUN add-apt-repository "deb [arch=amd64] https://dl.bintray.com/tetrate/getenvoy-deb $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y getenvoy-envoy

ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y nginx vim certbot python-certbot-nginx
ADD . /code/
ADD ./deploy/nginx/ /etc/nginx/
RUN ln -s /etc/nginx/sites-available/wateringcontrol_nginx.conf /etc/nginx/sites-enabled/

RUN chmod +x entry_point.sh
ENTRYPOINT [ "./entry_point.sh" ]