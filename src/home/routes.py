from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix="")


@home_bp.get("/")
def home():
    return "<b>Home page for the table generator application</b>"
