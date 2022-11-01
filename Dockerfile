# app/Dockerfile

FROM python:3.9-slim
EXPOSE 8501
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

RUN pip install -r requirements.txt
RUN pip install --upgrade --user git+https://github.com/GeneralMills/pytrends
RUN mkdir /home/seluser /home/seluser/downloads 

ENTRYPOINT ["streamlit", "run", "sos.py", "--server.port=8080","--server.address=0.0.0.0"]


