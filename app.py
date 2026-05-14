from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from db import conexion, cursor

app = Flask(__name__)
app.secret_key = "prospera_secret_key"


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        sql = "SELECT * FROM usuarios WHERE email = %s"
        valores = (email,)

        cursor.execute(sql, valores)
        usuario = cursor.fetchone()

        if usuario:

            if check_password_hash(usuario["password"], password):

                session["usuario"] = usuario["nombre"]

                return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Correo o contraseña incorrectos"
        )

    return render_template("login.html")



@app.route("/dashboard")
def dashboard():

    if "usuario" in session:
        return render_template(
            "dashboard.html",
            nombre=session["usuario"]
        )

    return redirect(url_for("login"))


#
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)