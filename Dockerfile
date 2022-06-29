FROM python:3.8.12-slim

RUN apt-get update -y && apt-get install tk -y

WORKDIR /Games
COPY [ "/Games/main.py " , "Games/Pong/pong.py", "." ]

ENTRYPOINT [ "python3", "main.py"]