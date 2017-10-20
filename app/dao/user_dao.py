# -*- coding: utf-8 -*-

import base_dao
from app.sql.user_info import save_user_info_sql, login_user_info_sql

run_sql_component = 'user_dao'

def save_user_info(user):
    sql_params = {'username': user.username, 'password': user.password}
    save_status = base_dao.savel_sql(run_sql_component, save_user_info_sql, sql_params)
    return save_status

def login_user_info(user):
    sql_params = {'username': user.username, 'password': user.password}
    user_info = base_dao.query_sql(run_sql_component, login_user_info_sql, sql_params)
    return user_info
