# -*- coding: utf-8 -*-

from flask import Blueprint, request, make_response
from app.model.user_info import UserInfo
import app.service.user_service as user_service
import json

uc = Blueprint('user_controller', __name__)


def response_headers(content):
    resp = make_response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
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
        rsp.mimetype = 'text/json'
        rsp.data = "注册成功"
        return rsp
    else:
        rsp.mimetype = 'text/json'
        rsp.data = "注册失败, 用户已存在"
        return rsp




@uc.route('/login')
def login():
    # params = request.args.get('uid', 'username', 'age','sex', 'status')
    params = request.args
    user = UserInfo(**params)
    print user
    print request.args
    print params
    rsp = make_response('login')
    rsp.mimetype = 'text/json'
    rsp.data = "11111"
    return rsp
