from flask import Flask, request
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

conn = None
cur = None

try:
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME,
                            user=DB_USERNAME, password=DB_PASSWORD)
    cur = conn.cursor()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

#############

db = SQLAlchemy(app)

Migrate(app, db)


####################


@app.route('/post/<id>', methods='GET')
def user_posts(id):

    else:
        return {"You are not allowed to post yet."}


if __name__ == '__main__':
    app.run(debug=True)
