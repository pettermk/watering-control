FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN chmod +x entry_point.sh
ENTRYPOINT [ "./entry_point.sh" ]