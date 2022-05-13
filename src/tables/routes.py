from crypt import methods
from flask import Blueprint, request
from models import Table

table_bp = Blueprint("table", __name__, url_prefix="/table")


@table_bp.route("/submit", methods=("POST",))
def submit_table_data():
    request_data = request.get_json()
    return str(Table(request_data))
