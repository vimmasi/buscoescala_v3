from flask import abort
from flask_restx import Resource, Namespace


from .schemas import (
    escala_schema,
    militar_schema,
    militar_post_schema,
)
from .extensions import db
from .models import Escala, Militar

# Definindo Namespaces para Swagger
escala_ns = Namespace("escala", description="Visualização de escalas")
militar_ns = Namespace("militar", description="Manipulação dos militares")


# Rotas para ESCALAS
@escala_ns.route("/escalas")
class EscalaListaAPI(Resource):
    @escala_ns.marshal_list_with(escala_schema)
    def get(self):
        """Listar todas as escalas"""
        return Escala.query.all()


@escala_ns.route("/escalas/<int:id>")
class EscalaAPI(Resource):
    @escala_ns.marshal_with(escala_schema)
    def get(self, id):
        """Buscar uma escala por ID"""
        escala = Escala.query.get(id)
        return escala


# Rotas para MILITARES
@militar_ns.route("/militares")
class MilitarListaAPI(Resource):
    @militar_ns.marshal_list_with(militar_schema)
    def get(self):
        """Listar todos os militares"""
        return Militar.query.all()

    @militar_ns.expect(militar_post_schema)
    @militar_ns.marshal_with(militar_schema)
    def post(self):
        """Postar um novo militar"""
        militar = Militar(
            patente=militar_ns.payload["patente"],
            nome=militar_ns.payload["nome"],
            escala_id=militar_ns.payload["escala_id"],
        )

        db.session.add(militar)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(
                500,
                "Ocorreu um erro ao salvar no banco de dados! Verifique as informações passadas.",
            )

        return militar, 201


@militar_ns.route("/militares/<int:id>")
class MilitarAPI(Resource):
    @militar_ns.marshal_with(militar_schema)
    def get(self, id):
        """Buscar um militar por ID"""
        militar = Militar.query.get(id)
        return militar

    @militar_ns.expect(militar_post_schema)
    @militar_ns.marshal_with(militar_schema)
    def put(self, id):
        """Atualizar um militar por ID"""
        militar = Militar.query.get(id)
        militar.patente = militar_ns.payload["patente"]
        militar.nome = militar_ns.payload["nome"]
        militar.escala_id = militar_ns.payload["escala_id"]

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(
                500,
                "Ocorreu um erro ao atualizar o banco de dados! Verifique as informações passadas.",
            )

        return militar, 201

    def delete(self, id):
        """Deletar um militar por ID"""
        militar = Militar.query.get(id)

        db.session.delete(militar)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(
                500,
                "Ocorreu um erro ao excluir o militar do banco de dados! Verifique as informações passadas.",
            )

        return {}, 204
