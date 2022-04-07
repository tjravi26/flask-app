from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# Database location setup

app.config['SECRET_KEY'] = 'potato'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB_HOST = 'localhost'
DB_NAME = 'fake_api'
DB_USERNAME = 'postgres'
DB_PASSWORD = '7890'

conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME,
                        user=DB_USERNAME, password=DB_PASSWORD)
cur = conn.cursor()


@app.route('/user/<id>')
def user_posts(id):
    cur.execute(f'SELECT title, body FROM posts WHERE id={id}')
    user_posts = cur.fetchall()
    return render_template('output.html', outputs=user_posts)


@app.route('/post/<id>')
def post_id(id):
    cur.execute(f'SELECT "userId" FROM posts WHERE id={id}')
    post_id = cur.fetchall()
    return render_template('output.html', outputs=post_id)


@app.route('/comment/<id>')
def comment_id(id):
    cur.execute(f'SELECT "postId" FROM comments WHERE id={id}')
    comment_id = cur.fetchall()
    return render_template('output.html', outputs=comment_id)


#############
db = SQLAlchemy(app)

Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
