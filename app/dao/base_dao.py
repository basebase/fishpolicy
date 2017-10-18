# -*- coding: utf-8 -*-

import app.db.mysql_engines
from app.db.mysql_engines import execute_sql, query_sql

def savel_sql(run_sql_component, sql, params):
    status = execute_sql(run_sql_component, sql, params)
    return status

def del_sql(run_sql_component, sql, params):
    status = execute_sql(run_sql_component, sql, params)
    return status

def update_sql(run_sql_component, sql, params):
    status = execute_sql(run_sql_component, sql, params)
    return status

def query(run_sql_component, sql, params):
    data = query_sql(run_sql_component, sql, params)
    return data