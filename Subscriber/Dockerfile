FROM node:18
WORKDIR /Subscriber

COPY package*.json ./
RUN npm install

EXPOSE 5672

COPY . .
CMD [ "node", "./src/receive-logs.js", "#" ]
