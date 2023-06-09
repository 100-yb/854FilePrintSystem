import mysql.connector
import os
from mysql.connector import errors
from flask import Flask,session
app = Flask(__name__, template_folder='../views/',
            static_folder='../static')
app.config['SECRET_KEY'] = os.urandom(24)
def connect_db():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root1234',
            auth_plugin='mysql_native_password',
            database='printshop',
        )
    except errors.ProgrammingError as e:
        print('数据库连接错误:', e)
        return None
    return conn
