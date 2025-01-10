from flask import Flask, render_template, url_for

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario)

@app.route("/cadastro")
def login():
    return render_template ("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)