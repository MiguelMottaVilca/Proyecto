from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

#TAREA NUEVA FUNCION RUTA HOMEWORK

@app.route("/homework", methods=["GET"])
def homework():
    name = request.form.get("name")
    return render_template("homework.html", name=name)

#  TAREA ROUTE
@app.route("/<string:name>")
def homework(name):
    return "Error 404 pagina no disponible"
