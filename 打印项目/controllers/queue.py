# -*- coding: utf-8 -*-
from utils import app
from flask import render_template
from models.print_model import get_queue_length


@app.route('/queue_length', methods=['GET'])
def get_queue_length_route():
    return str(get_queue_length())

@app.route('/queue', methods=['GET'])
def queue():
    queue_length = get_queue_length()
    return render_template('queue.html', queue_length=queue_length)
