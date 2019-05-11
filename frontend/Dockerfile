FROM node:lts-alpine

WORKDIR /app
COPY src ./src
COPY public ./public
COPY package.json package-lock.json ./
RUN npm install

CMD ["npm", "start"]
