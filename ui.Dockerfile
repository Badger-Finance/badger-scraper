FROM node:14.17.6-alpine
ARG V2_UI_READ_TOKEN
ENV APP_HOME /v2-ui
ENV NODE_OPTION --max-old-space-size=8192
WORKDIR $APP_HOME

RUN apk update
RUN apk add git

RUN git clone https://$V2_UI_READ_TOKEN:x-oauth-basic@github.com/Badger-Finance/v2-ui.git .
COPY wait_for_ui.sh ./
RUN yarn
RUN yarn global add serve
RUN yarn build
