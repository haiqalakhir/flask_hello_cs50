from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "world"

    #name = request.args.get("name", "world")  #ni cara pendek ganti if else
    #return render_template("index.html", name=name)
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)
