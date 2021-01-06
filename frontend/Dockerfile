FROM node:current-alpine3.12

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./

COPY package-lock.json ./

RUN npm i

COPY . ./

RUN npm run build

RUN npm install -g serve

ENV PORT=3000

EXPOSE 3000

CMD ["serve", "-s", "build"]
