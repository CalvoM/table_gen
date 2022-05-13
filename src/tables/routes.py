from crypt import methods
from flask import Blueprint, request
from models import Table
from flask_expects_json import expects_json

table_bp = Blueprint("table", __name__, url_prefix="/table")

table_schema = {
    "type" : "object",
    "properties": {
        "caption": {"type": "string"},
        "style": {"type": "string"}, # TODO: v2
        "headers": {"type": "array"}
    },
    "required": ["caption"]
}

@table_bp.route("/submit", methods=("POST",))
@expects_json(table_schema)
def submit_table_data():
    request_data = request.get_json()
    return str(Table(request_data))
