# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('/Users/Joker/Documents/my_code/python_code/fishpolicy/app')

from flask import Flask
from flask_request_params import bind_request_params
import controller.user_controller as uc
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.before_first_request(bind_request_params)


app.add_url_rule('/login', 'login', uc.login, methods=["POST", "GET"])
app.add_url_rule('/register', 'register', uc.register, methods=["POST", "GET"])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8088)
