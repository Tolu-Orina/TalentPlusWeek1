FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

RUN pip3  install Flask && pip3 install requests

EXPOSE 5000
CMD [ "python3", "app.py"]