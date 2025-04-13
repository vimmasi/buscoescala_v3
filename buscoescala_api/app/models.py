from sqlalchemy import CheckConstraint

from .extensions import db


class Escala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.String(50), nullable=False, unique=True)
    militares = db.relationship("Militar", backref="escala")


class Militar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patente = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    escala_id = db.Column(db.Integer, db.ForeignKey("escala.id"))

    # Validação de input
    __table_args__ = (
        CheckConstraint(
            "(escala_id IS NULL) OR (escala_id>=0 AND escala_id<=12)",
            name="escala_id_range",
        ),
    )
