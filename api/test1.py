
# -*- coding: UTF-8 -*-
from flask.views import MethodView
from flast.utils.response.R import R
from flast.utils.response.enums import Code
from flast.utils.response.msg_enum import SUCCESS_MSG
from flast.utils.error.decorated_error import handle_exceptions


class Test1Manager(MethodView):
    
    @handle_exceptions
    def post(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def get(self, obj, action=None):
        
        if action is not None:
            # Handle case where all optional args are provided
            pass
        else:
            # Handle case where some or no optional args are provided
            pass
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def delete(self, obj):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def put(self, obj):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    