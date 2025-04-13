# Busco Escala API

## 📌 Descrição

Este projeto é uma API desenvolvida como parte do MVP da Sprint 1 da PUC-Rio. Seu objetivo é facilitar o gerenciamento de militares e escalas de serviço, oferecendo endpoints RESTful para operações de criação, leitura, atualização e exclusão (CRUD).

## 🚀 Tecnologias Utilizadas

- Python 3.9
- Flask
- Flask-RESTX
- Docker

## 🛠️ Instalação e Execução Local

Para executar o projeto localmente, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/vimmasi/buscoescala_v3.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd buscoescala_v3/buscoescala_api
   ```

3. **Crie e ative o ambiente virtual:**

   - No Windows:

     ```bash
     py -3 -m venv venv
     venv\Scripts\activate
     ```

   - No Unix/MacOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o projeto:**

   ```bash
   flask run
   ```

6. **Acesse a aplicação:**

   Abra o navegador e vá para: [http://localhost:5000](http://localhost:5000)

> **Nota:** Caso ocorra o erro `While importing 'app', an ImportError was raised`, instale manualmente o Flask-RESTX:

```bash
pip install --upgrade flask-restx
```

## 🐳 Execução com Docker

Para executar a aplicação utilizando Docker, siga os passos abaixo:

1. **Construa a imagem Docker:**

   ```bash
   docker build -t buscoescala-api .
   ```

2. **Execute o container:**

   ```bash
   docker run -d -p 5001:5001 buscoescala-api
   ```

3. **Acesse a aplicação:**

   Abra o navegador e vá para: [http://localhost:5001](http://localhost:5001)

> **Nota:** A porta padrão exposta pelo container é a `5001`, conforme especificado no `Dockerfile`.

## 📚 Endpoints Disponíveis

A API está estruturada em dois namespaces principais: `militar` e `escala`. Abaixo estão as rotas atualmente implementadas:

### Militar

- **GET** `/militar/militares`  
  Retorna a lista de todos os militares.

- **GET** `/militar/militares/<id>`  
  Retorna os detalhes de um militar específico.

- **POST** `/militar/militares`  
  Cria um novo registro de militar.

- **PUT** `/militar/militares/<id>`  
  Atualiza as informações de um militar existente.

- **DELETE** `/militar/militares/<id>`  
  Remove um militar do sistema.

### Escala

- **GET** `/escala/escalas`  
  Retorna a lista de todas as escalas.

- **GET** `/escala/escalas/<id>`  
  Retorna os detalhes de uma escala específica.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de novas rotas, melhorias na estrutura do código ou qualquer outra ideia para aprimorar o projeto, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto é de uso livre.
