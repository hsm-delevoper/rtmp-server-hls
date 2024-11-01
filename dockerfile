
FROM node:14-alpine


WORKDIR /app


COPY package.json .


RUN npm install


COPY . .


RUN apk add --no-cache ffmpeg


EXPOSE 1935 8000


CMD ["node", "index.js"]