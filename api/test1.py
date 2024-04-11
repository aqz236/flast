
# -*- coding: UTF-8 -*-
from flask.views import MethodView
from utils.response.R import R
from utils.response.enums import Code
from utils.response.msg_enum import SUCCESS_MSG
from utils.error.decorated_error import handle_exceptions


class Test1Manager(MethodView):
    
    @handle_exceptions
    def post(self):
        
        # Write the implementation details here
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def get(self, obj, action=None):
        
        if action is not None:
            pass
        else:
            pass
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def delete(self, obj, name=None):
        
        if name is not None:
            pass
        else:
            pass
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def put(self, obj, name=None):
        
        if name is not None:
            pass
        else:
            pass
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    