#! /usr/bin/python3

import sqlite3

from flask import Flask, render_template
app = Flask(__name__)

DB = "/var/lib/fail2ban/fail2ban.sqlite3"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/showBans')
def show_bans():
    cur = get_db().cursor()

    all_bans = []

    for ban in query_db("select ip,jail from bips"):
        all_bans.append((ban["ip"], ban["jail"]))

    return render_template("show_bans.html", all_bans=all_bans)

if __name__ == '__main__':
    app.run(debug=False)

