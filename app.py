from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'potato'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

posts_url = 'https://jsonplaceholder.typicode.com/posts'
comments_url = 'https://jsonplaceholder.typicode.com/comments'
users_url = 'https://jsonplaceholder.typicode.com/users'


if __name__ == '__main__':
    app.run(debug=True)
