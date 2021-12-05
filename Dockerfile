FROM python:3.9-slim-buster

RUN apt-get update
RUN apt-get install -y gnupg2
RUN apt-get install -y wget

ENV CHROMEDRIVER_PATH=/usr/local/bin/
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

RUN apt-get install -yqq unzip curl
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d $CHROMEDRIVER_PATH

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /scraper_bot
WORKDIR $APP_HOME
COPY . ./

RUN pip install --upgrade pip
RUN pip install -r ./scraper/requirements/requirements.txt -r ./scraper/requirements/requirements-dev.txt
