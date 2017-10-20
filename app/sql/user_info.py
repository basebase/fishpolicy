# -*- coding: utf-8 -*-

save_user_info_sql = """
    INSERT INTO user_info VALUES (NULL, '$username', MD5('$password'))
"""

login_user_info_sql = """
    SELECT
        username
    FROM
        user_info
    WHERE
        username = '$username' AND
        password = MD5('$password')
"""