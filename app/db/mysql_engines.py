from string import Template

import mysql.connector
import pandas as pd

from app.config.mysql_config import mysql_dev_config


def get_dev_connection(config):
    conn = mysql.connector.Connect(**config)
    return conn

def execute_sql(run_sql_component, sql, params = None):
    try:
        conn = get_dev_connection(mysql_dev_config)
        save_cursor = conn.cursor()
        sql = Template(sql).substitute(params)

        print run_sql_component + " Run SQL => " + sql

        save_cursor.execute(sql)
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print ex
        return False

def query_sql(sql, params = None):
    conn = get_dev_connection(mysql_dev_config)
    sql = Template(sql).substitute(params)
    df = pd.read_sql(sql, conn)
    return df