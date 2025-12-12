
from flask import render_template
from app import app

@app.route("/cadastro")
def cadastro():
    return render_template("/cliente/formulario.html")