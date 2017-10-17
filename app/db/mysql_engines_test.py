# -*- coding: utf-8 -*-
import sys
import os
from string import Template
import mysql_engines

sql = """
    INSERT INTO user_info VALUES(NULL,'b','b')
"""


sql2 = """
    SELECT username as uname, password from user_info
"""

if __name__ == '__main__':
    # params = {'age': '33', 'date': '2016-05-07'}

    save_status = mysql_engines.query_sql(sql2, params=None)
    js = save_status.to_json(orient='records')
    print js