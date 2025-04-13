# Busco Escala API

## Descrição

Projeto MPV Sprint 1 da PUC-Rio, essa API visa facilitar o gerenciamento de militares e escalas de serviço.

## Instalação

Siga estas etapas para instalar e executar o projeto localmente:

1. Clone o repositório:
    ```
    git clone https://github.com/vimmasi/buscoescala_api.git
    ```
2. Navegue até o diretório do projeto:
    ```
    cd buscoescala_api
    ```
3. Crie o ambiente virtual:
    ```
    py -3 -m venv venv
    ```
3. Inicie o ambiente virtual:
    ```
    .venv\Scripts\activate
    ```
4. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
5. Execute o projeto:
    ```
    flask run
    ```
6. Acesse o projeto:
    ```
    http://localhost:5000
    ```
7. (opcional) Caso retorne o erro chamado `While importing 'app', an ImportError was raised`, nesse caso instale o Flask Restx manualmente:
    ```
    pip install flask-restx
    ```

## Uso

Os endpoints são separados em 2 namespaces:
- militar
- escala

Temos as seguintes rotas implementadas:

### GET 
> /militar/militares

> /militar/militares/\<id>

> /escala/escalas

> /escala/escalas/\<id>

### POST 
> /militar/militares

### PUT 
> /militar/militares/\<id>

### DELETE 
> /militar/militares/\<id>


## Contribuição

Ideias sobre como implementar mais rotas ou minimizar a quantidade de código, as ideias 

## Licença

Esse projeto é de uso livre.
