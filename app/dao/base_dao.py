# -*- coding: utf-8 -*-

import app.db.mysql_engines
from app.db.mysql_engines import execute_sql, query_sql

def savel_sql(sql, params):
    status = execute_sql(sql, params)
    return status

def del_sql(sql, params):
    status = execute_sql(sql, params)
    return status

def update_sql(sql, params):
    status = execute_sql(sql, params)
    return status

def query(sql, params):
    data = query_sql(sql, params)
    return data