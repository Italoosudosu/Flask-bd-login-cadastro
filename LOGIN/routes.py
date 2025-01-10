#ROTAS DO SITE
from flask import render_template, url_for
from LOGIN import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario)

@app.route("/cadastro")
def login():
    return render_template ("cadastro.html")
