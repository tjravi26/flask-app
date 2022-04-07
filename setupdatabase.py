from app import db
import json
import requests


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


def json_api_posts():
    fake_api_url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(fake_api_url)
    output = json.loads(r.text)
    return output


def json_api_users():
    fake_api_url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(fake_api_url)
    output = json.loads(r.text)
    return output


def json_api_comments():
    fake_api_url = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(fake_api_url)
    output = json.loads(r.text)
    return output


posts_data = json_api_posts()
users_data = json_api_users()
comments_data = json_api_comments()


def update_data(posts_data, users_data, comments_data):
    final_users_data = []
    final_posts_data = []
    final_comments_data = []
    for data in range(len(users_data)):
        new_entry = Users(id=users_data[data]['id'],
                          name=users_data[data]['name'],
                          username=users_data[data]['username'],
                          email=users_data[data]['email'],
                          phone=users_data[data]['phone'],
                          website=users_data[data]['website'])
        final_users_data.append(new_entry)
    for data in range(len(posts_data)):
        new_entry = Posts(id=posts_data[data]['id'],
                          userId=posts_data[data]['userId'],
                          title=posts_data[data]['title'],
                          body=posts_data[data]['body'])
        final_posts_data.append(new_entry)

    for data in range(len(comments_data)):
        new_entry = Comments(id=comments_data[data]['id'],
                             postId=comments_data[data]['postId'],
                             name=comments_data[data]['name'],
                             email=comments_data[data]['email'],
                             body=comments_data[data]['body'])
        final_comments_data.append(new_entry)
    db.create_all()
    db.session.add_all(final_users_data)
    db.session.add_all(final_posts_data)
    db.session.add_all(final_comments_data)
    db.session.commit()


update_data(posts_data, users_data, comments_data)
