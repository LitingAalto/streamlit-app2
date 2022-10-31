# app/Dockerfile

FROM python:3.9-slim
EXPOSE 8501
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

# RUN apt-get update && \
#     apt-get install -y gnupg wget curl unzip --no-install-recommends && \
#     wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#     echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
#     apt-get update -y && \
#     apt-get install -y google-chrome-stable && \
#     CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
#     DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
#     wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
#     unzip /chromedriver/chromedriver* -d /chromedriver

RUN pip install -r requirements.txt
RUN mkdir /home/seluser /home/seluser/downloads 

ENTRYPOINT ["streamlit", "run", "sos.py", "--server.port=8080","--server.address=0.0.0.0"]


