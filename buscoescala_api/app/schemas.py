from flask_restx import fields

from .extensions import api


militar_schema = api.model(
    "Militar",
    {
        "id": fields.Integer,
        "patente": fields.String,
        "nome": fields.String,
        "escala_id": fields.Integer,
    },
)

escala_schema = api.model(
    "Escala",
    {
        "id": fields.Integer,
        "mes": fields.String,
        "militares": fields.List(fields.Nested(militar_schema)),
    },
)

# escala_post_schema = api.model("EscalaPost", {"mes": fields.String})

militar_post_schema = api.model(
    "MilitarPost",
    {"patente": fields.String, "nome": fields.String, "escala_id": fields.Integer},
)
