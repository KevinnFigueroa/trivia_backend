"""
from flask_sqlalchemy import SQLAlchemy


class InitModels:
    def __init__(self, app):
        db = SQLAlchemy(app)
        instance = db.Model
        UsersModel(instance)


class UsersModel(db.Model):
    __tablename__ = "users"

    print("llega aqui")
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.Integer())

    # def __init__(self, app):
    #    self.name = name
    #    self.username = model
    #    self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"
"""