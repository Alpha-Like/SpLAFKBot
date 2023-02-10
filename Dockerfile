FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get -y update

RUN apt-get -y install git

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["bash", "yashu.sh"]

EXPOSE 8080
