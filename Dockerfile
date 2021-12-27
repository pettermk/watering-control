FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y debian-keyring debian-archive-keyring apt-transport-https curl lsb-release
RUN curl -sL 'https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key' | gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg
RUN echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/debian $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/getenvoy.list
RUN apt-get update
RUN apt-get install -y getenvoy-envoy

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN chmod +x entry_point.sh
ENTRYPOINT [ "./entry_point.sh" ]