from flask import (
    Flask,
    json,
    jsonify,
    make_response,
    render_template,
    request,
    redirect,
)
from flask.json import dumps
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db.database import initDb

app = Flask(__name__)

initDb(app)


@app.route("/", methods=["GET"])
def index():
    print("ahre")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    data = {"user": "kevin"}
    response = app.response_class(
        response=json.dumps(data), status=200, mimetype="application/json"
    )
    return response


# TODO: para establecer los 5 mejores debo usar signals


@app.route("/ranking", methods=["GET"])
def ranking():
    data = {"topFive": ["kevin", "renzo", "german", "pablo", "walter"]}
    response = app.response_class(
        response=json.dumps(data), status=200, mimetype="application/json"
    )
    return response


@app.route("/random_trivia", methods=["GET"])
def random_trivia():
    data = {"Amor": "Palabra de afecto hacia otra persona"}

    response = app.response_class(
        response=json.dumps(data), status=200, mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
