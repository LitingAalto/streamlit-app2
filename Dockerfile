# app/Dockerfile

FROM python:3.9-slim
EXPOSE 8501
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y libglib2.0-0=2.50.3-2 \
    libnss3=2:3.26.2-1.1+deb9u1 \
    libgconf-2-4=3.2.6-4+b1 \
    libfontconfig1=2.11.0-6.7+b1


RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "sos.py", "--server.port=8080","--server.address=0.0.0.0"]


