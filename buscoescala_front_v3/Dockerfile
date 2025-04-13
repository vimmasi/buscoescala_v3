# Etapa 1: build
FROM node:18 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Etapa 2: servir com nginx
FROM nginx:alpine

# Copia o build do Vue para o nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Copia config padrão do nginx (opcional, usa a default se não tiver)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
