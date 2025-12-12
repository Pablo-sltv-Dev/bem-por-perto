from flask import render_template
from app import app


@app.route("/cuidador")
def cuidador():
    return render_template("/cuidador/cadast.html")