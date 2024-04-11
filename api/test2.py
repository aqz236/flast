
# -*- coding: UTF-8 -*-
from flask.views import MethodView
from utils.response.R import R
from utils.response.enums import Code
from utils.response.msg_enum import SUCCESS_MSG
from utils.error.decorated_error import handle_exceptions


class Test2Manager(MethodView):
    
    @handle_exceptions
    def post(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def get(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def put(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def delete(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def patch(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def head(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    
    @handle_exceptions
    def options(self):
        
        # 在此编写实现细节
        
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    