# -*- coding: utf-8 -*-
from  utils import app
from flask import redirect, url_for, render_template, request
from utils import connect_db
from mysql.connector import errors

@app.route('/register.html')
def register_html():
    return render_template('register.html')
@app.route('/register',methods=['post'])
def register():
    print(request.form.to_dict())
    userid = request.form.get('userid')
    username = request.form.get('username')
    password = request.form.get('password')
    message = ""
    if username ==None or password==None:
        message = "用户名或密码不能为空!"
    elif not userid.isdigit():
        message = "用户id必须为数字!"
    else:
        try:
            # Insert the print file information into the database
            conn = connect_db()
            cursor = conn.cursor()
            query = "INSERT INTO printuser (userid, username, password, permission) VALUES (%s, %s, %s, %s)"
            values = (userid, username, password, 'common')
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('login'))  # Redirect to the queue length display page
        except errors.DatabaseError as e:
            print('数据库操作错误:', e)
    return render_template('register.html',message='请检查表单,注册失败!')
