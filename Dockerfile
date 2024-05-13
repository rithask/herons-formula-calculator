# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod -x entrypoint.sh

EXPOSE 8000

CMD ["sh", "entrypoint.sh"]
