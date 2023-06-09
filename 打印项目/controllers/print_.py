# -*- coding: utf-8 -*-
from models.print_model import connect_db, get_queue_length, print_file, print_first_file
from flask import render_template, redirect, url_for, request,session
from mysql.connector import errors
import datetime
import os
import threading
import time
from utils import app

@app.route('/print', methods=['GET', 'POST'])
def print_1():
    if request.method == 'POST':
        username = request.form.get('username')
        file = request.files['file']
        filename = file.filename
        file.save('./tmp/tmp_'+filename)
        session['file'] = os.getcwd()+'/tmp/tmp_'+filename
        print(session['file'])
        print(filename)
        filedata = file.read()
        filesize = len(filedata)
        side = request.form.get('side')
        color = request.form.get('color')
        copies = int(request.form.get('copies'))

        session['side'] = side
        session['color'] = color
        session['copies'] =copies

        # Connect to the database
        conn = connect_db()
        if not conn:
            return render_template('print.html', error='数据库连接错误')

        # Get the current time
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            # Insert the print file information into the database
            cursor = conn.cursor()
            query = "INSERT INTO printfile (file, filename, filesize, createtime, userid, copies, side, color) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (filedata, filename, filesize, current_time, 1, copies, side, color)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('print_first'))  # Redirect to the queue length display page
        except errors.DatabaseError as e:
            if 'Duplicate' in str(e):
                print("已存在!")
                return redirect(url_for('print_first'))  # Redirect to the queue length display page
            return render_template('print.html', error='数据库操作错误')
    else:
        username = request.args.get('username')
        # Display the print page
        return render_template('print.html')

@app.route('/print_first', methods=['GET'])
def print_first():
    # Get the queue length before printing
    initial_queue_length = get_queue_length()
    print(session['color'],session['copies'],session['side'])

    # Start the printing operation in a separate thread
    threading.Thread(target=print_first_file).start()

    # Wait for the printing to finish
    time.sleep(5)  # Assume that the printing operation takes 5 seconds to complete, you can adjust the waiting time according to the actual situation

    # Get the queue length after printing
    updated_queue_length = get_queue_length()

    # Update the queue length
    if updated_queue_length < initial_queue_length:
        queue_length = updated_queue_length
    else:
        queue_length = initial_queue_length

    return render_template('queue.html', queue_length=queue_length)
