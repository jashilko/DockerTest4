from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world1():
    return "<h1>Hello, World<h1>"

@app.route('/db')
def hello_world():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="user",
        password="password",
        host="db1"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Hello, World! Database version: {db_version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)