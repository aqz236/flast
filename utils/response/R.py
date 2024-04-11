# -*- coding: UTF-8 -*-

# utils/response/R.py

class R:
    def __init__(self):
        self._result = {}

    def msg(self, message=''):
        self._result['msg'] = message
        return self

    def code(self, error_code):
        self._result['code'] = error_code.value
        return self

    def data(self, data=None):
        if data is None:
            data = {}
        self._result['data'] = data
        return self

    def build(self):
        return self._result
