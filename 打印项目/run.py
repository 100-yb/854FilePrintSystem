#
from flask import Flask
from utils import app
from controllers import *


if __name__ == '__main__':
    app.run(debug=True)
