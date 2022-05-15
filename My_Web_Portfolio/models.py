from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    pwdhash = db.Column(db.String(54))

    def __init__(self, Name, password):
        self.Name = Name.title()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
