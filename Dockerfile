FROM python:3.8.7

ENV PYTHONUNBUFFERED 1

ENV APP_HOME /scraper_bot
WORKDIR $APP_HOME
COPY . ./

RUN pip install --upgrade pip
RUN pip install -r ./scraper/requirements/requirements.txt -r ./scraper/requirements/requirements-dev.txt
