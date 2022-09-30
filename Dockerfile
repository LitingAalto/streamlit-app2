# app/Dockerfile

FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential



RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "sos.py"]


