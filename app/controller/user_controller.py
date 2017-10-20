# -*- coding: utf-8 -*-

from flask import Blueprint, request, make_response, jsonify
from app.model.user_info import UserInfo
import app.service.user_service as user_service
import json

uc = Blueprint('user_controller', __name__)


def response_headers(content):
    resp = make_response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.mimetype = 'application/json'
    return resp

@uc.route('/register', methods=["POST", "GET"])
def register():
    '用户注册函数'

    params = json.loads(request.data) # 获取到用户输入的全部参数

    username = params.get('username')
    password = params.get('password')

    user = UserInfo(username, password)

    status = user_service.save_user_info(user)

    rsp = response_headers('register')

    if status:
        # rsp.mimetype = 'text/json'
        return jsonify({"msg_info": "注册成功", "register_type": True})
    else:
        return jsonify({"msg_info": "注册成功", "register_type": True})



@uc.route('/login')
def login():
    params = json.loads(request.data)  # 获取到用户输入的全部参数
    user = UserInfo(**params)
    user_df = user_service.login_user_info(user)

    print user_df

    data = user_df['username']

    return jsonify({"msg_info": "登录成功", "login_type": True, "username": data})