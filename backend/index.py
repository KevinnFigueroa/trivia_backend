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

import os
from firebase_admin import credentials, firestore, initialize_app

from services.get_words_api import RandomTrivia

app = Flask(__name__)

initDb(app)

# Initialize Firestore DB
cred = credentials.Certificate("./serviceAccountKey.json")
default_app = initialize_app(cred)
db = firestore.client()
users = db.collection("users")

# Initialize Trivia API
instance = RandomTrivia()


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


@app.route("/list", methods=["GET"])
def read():
    """
    read() : Fetches documents from Firestore collection as JSON
    todo : Return document that matches query ID
    all_todos : Return all documents"""
    try:
        all_todos = [doc.to_dict() for doc in users.stream()]
        return jsonify(all_todos), 200

    except Exception as e:
        return f"An Error Occured: {e}"


# TODO: para establecer los 5 mejores debo usar signals


@app.route("/ranking", methods=["GET"])
def ranking():
    # Hacer consulta a firebase de los users que tienen qualification más altos
    data = {"topFive": ["kevin", "renzo", "german", "pablo", "walter"]}
    response = app.response_class(
        response=json.dumps(data), status=200, mimetype="application/json"
    )
    return response


@app.route("/random_trivia", methods=["GET"])
def random_trivia():
    trivias = instance.get_random_trivia()

    if trivias:
        response = app.response_class(
            response=json.dumps(trivias), status=200, mimetype="application/json"
        )
        return response
    else:
        response = app.response_class(
            response=json.dumps({"Success": False}),
            status=404,
            mimetype="application/json",
        )
        return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
