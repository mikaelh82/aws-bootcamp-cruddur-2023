FROM node:16.8

ENV PORT=3000

WORKDIR /frontend-react-js


COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE ${PORT}

CMD ["npm", "start"]