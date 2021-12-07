FROM node:14-buster-slim
ARG V2_UI_READ_TOKEN
ENV APP_HOME /v2-ui
WORKDIR $APP_HOME

RUN apt-get update
RUN apt-get install -y git
RUN echo $V2_UI_READ_TOKEN

RUN git clone https://$V2_UI_READ_TOKEN:x-oauth-basic@github.com/Badger-Finance/v2-ui.git .
RUN yarn
