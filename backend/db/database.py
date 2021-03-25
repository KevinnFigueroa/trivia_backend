from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_utils import EmailType, PasswordType
import datetime


class initDb:
    print("llegue a init db")

    def __init__(self, app):
        app.config[
            "SQLALCHEMY_DATABASE_URI"
        ] = "postgresql://ultraapp:ultraapp*123@localhost:5432/trivia_app"

        db = SQLAlchemy(app)
        migrate = Migrate(app, db)

        class UsersModel(db.Model):
            __tablename__ = "users"

            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String())
            username = db.Column(db.String())
            password = db.Column(
                PasswordType(
                    schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"]
                )
            )
            email = db.Column(EmailType, nullable=False)
            qualification = db.Column(db.Float())
            last_login = db.Column(db.Time())
            create_datetime = db.Column(db.Time())

            def __init__(
                self,
                name,
                username,
                email,
                password,
                create_datetime,
                last_login,
                qualification,
            ):
                self.name = name
                self.username = username
                self.email = email
                self.password = password
                self.create_datetime = datetime.now()
                self.last_login = datetime.now()
                self.qualification = qualification or None

            def login_user(self, username, password):
                print("llegue a login")
                pass

            def __repr__(self):
                return f"<User {self.name}>"