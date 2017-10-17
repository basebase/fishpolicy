# -*- coding: utf-8 -*-

from app.model.user_info import UserInfo
import app.dao.user_dao as user_dao


def save_user_info(user_info):
    '保存注册用户'
    status = user_dao.save_user_info(user_info)
    return status
