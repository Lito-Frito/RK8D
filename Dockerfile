FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 \
    python3-tk

WORKDIR /Games
COPY /Games .

CMD export DISPLAY =":0"

ENTRYPOINT [ "python3", "main.py"]