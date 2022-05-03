from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
import sqlite3
import os
from database import connect_db, TelestatDB

SECRET_KEY = 'fffjjdhhndj33gitgits8fc8d3d'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST' and request.form['login'] == 'admin' and request.form['password'] == 'qwerty123':
        session['userLogged'] = request.form['login']
        return redirect(url_for('admin'))
    return render_template('index.html')

@app.route('/users-base', methods=['POST', 'GET'])
def users_base():
    db = connect_db()
    dbase = TelestatDB(db)
    rows = []
    if request.method == 'POST':
        if request.form['search']:
            rows = dbase.search_users(request.form['search'])
        #elif request.form['btn'] == 'choice':

    return render_template('users-base.html', action='/users-base', rows=rows)

@app.route('/admin')
def admin():
    if 'userLogged' not in session :
        return render_template('index.html')
    return render_template('admin.html')

@app.route('/composition')
def composition():
    if 'userLogged' not in session:
        return render_template('index.html')
    return render_template('composition.html')
app.run(debug=True)