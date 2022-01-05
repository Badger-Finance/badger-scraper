FROM node:16.13.1-alpine
ARG V2_UI_READ_TOKEN
ENV APP_HOME /v2-ui
ENV NODE_OPTION --max-old-space-size=8192
ENV GENERATE_SOURCEMAP false
WORKDIR $APP_HOME

RUN apk update
RUN apk add git
RUN apk add curl
RUN apk add coreutils

RUN git clone https://$V2_UI_READ_TOKEN:x-oauth-basic@github.com/Badger-Finance/v2-ui.git .
COPY wait_for_ui.sh ./
COPY run_ui.sh ./
RUN yarn
RUN yarn global add serve
RUN yarn build
