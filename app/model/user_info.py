# -*- coding: utf-8 -*-

import json

class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __set__(self, key, value):
        self.key = value

    def __get__(self, key, type=None):
        return self.key

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



