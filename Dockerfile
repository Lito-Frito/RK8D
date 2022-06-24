FROM python:3.8.12-slim

RUN apt-get update -y

RUN apt-get install tk -y

WORKDIR /Games
COPY /Games .

ENTRYPOINT [ "python3", "main.py"]