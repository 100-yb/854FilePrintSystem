# -*- coding: utf-8 -*-
from  utils import app
from flask import redirect, url_for, render_template, request
from utils import connect_db


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/funturn')
def funturn_page():
    return render_template('funturn.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    # Connect to the database
    conn = connect_db()
    if not conn:
        return render_template('login.html', error='数据库连接错误')
    # Check if the user exists in the users table
    cursor = conn.cursor()
    query = "SELECT password  FROM printuser WHERE userid=%s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    if user and password == user[0]:

        #return redirect(url_for('print_1'))
        return render_template('welcome you.html')
    else:
        return render_template('login.html', error='用户名或密码错误')

@app.route('/print_or_copy/<option>')
def print_or_copy(option):
    if option=='copy':
        return render_template('copy.html')
    if option=='print':
        return redirect(url_for('print_1'))