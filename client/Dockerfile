FROM node:10
RUN mkdir /client
WORKDIR /client
COPY package.json /client/package.json
RUN apt-get update -qq && apt-get install -y build-essential nodejs

RUN npm install