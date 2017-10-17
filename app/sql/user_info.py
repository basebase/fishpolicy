# -*- coding: utf-8 -*-

save_user_info_sql = """
    INSERT INTO user_info VALUES (NULL, '$username', MD5('$password'))
"""