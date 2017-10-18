# -*- coding: utf-8 -*-

import base_dao
from app.sql.user_info import save_user_info_sql

run_sql_component = 'user_dao'

def save_user_info(user):
    sql_params = {'username': user.username, 'password': user.password}
    save_status = base_dao.savel_sql(run_sql_component, save_user_info_sql, sql_params)
    return save_status