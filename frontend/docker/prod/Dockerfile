FROM node:20-alpine as builder

WORKDIR /app

COPY package*.json ./
COPY tsconfig*.json ./
COPY vite.config.ts ./
COPY src ./src
COPY public ./public
COPY index.html ./

RUN npm install
RUN npm run build

HEALTHCHECK --interval=5s --timeout=5s --start-period=1s CMD curl --fail http://127.0.0.1:5173/health || exit 1

FROM nginx:1.17-alpine

COPY --from=builder /app/dist /usr/share/nginx/html

COPY ./docker/dev/nginx/conf.d /etc/nginx/conf.d

# CMD ["npm", "run", "dev"]