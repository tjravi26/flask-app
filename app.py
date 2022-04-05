import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is atomatically set to basic.py with the above code


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'site.db')  # <-- Database location setup
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
