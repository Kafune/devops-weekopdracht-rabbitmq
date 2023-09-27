FROM node:18
WORKDIR /Subscriber 
EXPOSE 8080

COPY package*.json ./
RUN npm install

COPY . .
CMD [ "node", "./src/receive-subscription-topic.js" "#"]
