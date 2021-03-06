from crypt import methods
from unittest import result
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__)

# <-- Database location setup
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:7890@localhost/fake_api')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


####################


# Model - AKA Table in database
class Users(db.Model):

    # MANUAL TABLE NAME CHOICE!
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String(50))
    website = db.Column(db.String)

    def __init__(self, id, name, username,
                 email, phone, website):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website
    db.create_all()


class Posts(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String)
    body = db.Column(db.String)

    def __init__(self, id, userId, title, body):
        self.id = id
        self.userId = userId
        self.title = title
        self.body = body
    db.create_all()


class Comments(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer)
    name = db.Column(db.String)
    email = db.Column(db.String)
    body = db.Column(db.String)

    def __init__(self, id, postId, name, email, body):
        self.id = id
        self.postId = postId
        self.name = name
        self.email = email
        self.body = body
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
