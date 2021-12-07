FROM node:14-buster-slim
ARG V2_UI_READ_TOKEN
ENV APP_HOME /v2-ui
ENV NODE_OPTION --max-old-space-size=8192
WORKDIR $APP_HOME

RUN apt-get update
RUN apt-get install -y git
RUN echo $V2_UI_READ_TOKEN

RUN git clone https://$V2_UI_READ_TOKEN:x-oauth-basic@github.com/Badger-Finance/v2-ui.git .
RUN yarn
RUN yarn global add serve
RUN node --max_old_space_size=12288 node_modules/.bin/react-scripts build
