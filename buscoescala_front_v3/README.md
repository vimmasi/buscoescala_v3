# BuscoEscala v4

**BuscoEscala v4** é uma aplicação web desenvolvida com [Vue 3](https://vuejs.org/) e [Vite](https://vitejs.dev/), projetada para facilitar a busca e visualização de escalas de trabalho.

## 🚀 Tecnologias Utilizadas

- [Vue 3](https://vuejs.org/): Framework progressivo para construção de interfaces de usuário.
- [Vite](https://vitejs.dev/): Ferramenta de build rápida e moderna para projetos web.
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript): Linguagem de programação utilizada no desenvolvimento.
- [Node.js](https://nodejs.org/): Ambiente de execução para o JavaScript no servidor.
- [Docker](https://www.docker.com/): Plataforma para criação, envio e execução de containers.

## 📦 Instalação

### **Instalar Dependências**

1. Clone o repositório:

   ```bash
   git clone https://github.com/vimmasi/buscoescala_v4.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd buscoescala_v4
   ```

3. Instale as dependências:

   ```bash
   npm install
   ```

### **Executar Localmente (Desenvolvimento)**

Para iniciar o servidor de desenvolvimento com hot-reload:

```bash
npm run dev
```

## 🐳 Docker

### **Dockerizando a Aplicação**

O projeto já está configurado para ser executado em um container Docker.

#### **1. Criando a Imagem Docker**

Na raiz do projeto, execute:

```bash
sudo docker build -t buscoescala .
```

#### **2. Rodando o Container**

Após o build da imagem, rode o container:

```bash
sudo docker run -d -p 8080:80 buscoescala
```

Isso fará com que a aplicação fique disponível em:  
👉 [http://localhost:8080](http://localhost:8080)

#### **3. Parar o Container**

Para parar o container que está rodando, use o comando:

```bash
sudo docker stop <CONTAINER_ID>
```

Você pode pegar o `CONTAINER_ID` com:

```bash
sudo docker ps
```

Para remover o container, depois de parar:

```bash
sudo docker rm <CONTAINER_ID>
```

Ou para parar e remover de uma vez:

```bash
sudo docker rm -f <CONTAINER_ID>
```

### **nginx.conf**

Adicionei o arquivo de configuração `nginx.conf` para resolver conflitos de SPA do Vue.

## 📁 Estrutura do Projeto

```bash
buscoescala_v4/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── views/
│   └── main.js
├── Dockerfile
├── nginx.conf
├── package.json
├── vite.config.js
└── README.md
```

## 📄 Licença

Este projeto é de licença livre.
