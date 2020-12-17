import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return open("index.html", "rb").read()

@app.route("/<path:r>")
def route(r):
    return open(r, "rb").read()

if __name__ == "__main__":
    app.run(port = 8000, debug = True)
