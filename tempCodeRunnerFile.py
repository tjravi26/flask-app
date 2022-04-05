from app import Posts, Users, Comments, db, Migrate
import json
import requests


def json_api_posts():
    fake_api_url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(fake_api_url)
    posts_data = json.loads(r.text)


def json_api_users():
    fake_api_url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(fake_api_url)
    users_data = json.loads(r.text)


def json_api_comments():
    fake_api_url = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(fake_api_url)
    comments_data = json.loads(r.text)


# CREATES ALL THE TABLES Model --> Db Table
# Transforms your Model class to a database table
db.create_all()
