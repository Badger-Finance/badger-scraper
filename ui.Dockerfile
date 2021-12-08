FROM node:16-alpine
ARG V2_UI_READ_TOKEN
ENV APP_HOME /v2-ui
ENV NODE_OPTION --max-old-space-size=8192
WORKDIR $APP_HOME

RUN apk update
RUN apk add git

RUN git clone https://$V2_UI_READ_TOKEN:x-oauth-basic@github.com/Badger-Finance/v2-ui.git .
RUN yarn
RUN yarn global add serve
RUN yarn react-scripts --max_old_space_size=8092 build
