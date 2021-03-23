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


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://ultraapp:ultraapp*123@localhost:5432/trivia_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# TODO: debo pasar toda la lógica de base de datos a la carpeta "db"


class CarsModel(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


@app.route("/", methods=["GET"])
def index():
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
