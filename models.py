from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique = True)
    pwdhash= db.Column(db.String(54))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


class Gem(db.Model):
    __tablename__ = 'gems'
    uid = db.Column(db.Integer, primary_key = True)
    color = db.Column(db.String(100))
    luster = db.Column(db.String(100))
    fracture = db.Column(db.String(100))
    streak = db.Column(db.String(100))
    mohs = db.Column(db.Float())
    ri = db.Column(db.Float())
    specific_gravity = db.Column(db.Float())
    fluorescent = db.Column(db.Boolean())

    def __init__(self, color, luster, fracture, streak, mohs, ri, specific_gravity, fluorescent):
        self.color = color
        self.luster = luster
        self.fracture = fracture
        self.streak = streak
        self.mohs = mohs
        self.ri = ri
        self.specific_gravity = specific_gravity
        self.fluorescent = fluorescent
