from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tarea", methods=["POST","GET"])
def hello():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template( "tarea.html" , name=name) 
    else:    
        return render_template("error.html")

