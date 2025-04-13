from flask import Flask
from flask_cors import CORS

from .extensions import api, db
from .routes import militar_ns, escala_ns


# Criação do APP, no modo Factory Pattern
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuração SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///buscoescala.db"

    # Inicialização do app
    api.init_app(
        app,
        title="Busco Escala API",
        description="API de gerenciamento de escalas e militares",
        version="1.0",
        validate=True,
    )
    db.init_app(app)

    # Adição dos namespaces para swagger
    api.add_namespace(militar_ns)
    api.add_namespace(escala_ns)

    return app
