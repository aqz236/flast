import os
from jinja2 import Environment, FileSystemLoader
from flast.utils.config import ConfigUtil

config_json = ConfigUtil().get_config()

flask_blueprint_template = """
# -*- coding: UTF-8 -*-
from flask.views import MethodView
from flast.utils.response.R import R
from flast.utils.response.enums import Code
from flast.utils.response.msg_enum import SUCCESS_MSG
from flast.utils.error.decorated_error import handle_exceptions
\n
class {{ class_name }}(MethodView):
    {% for method_func, method_detail in methods.items() %}
    @handle_exceptions
    def {{ method_func }}(self{% if method_detail.arg_list %}, {{ method_detail.arg_list }}{% endif %}):
        {% if method_detail.arg_details %}
        {{ method_detail.arg_details|trim }}
        {% else %}
        # 在此编写实现细节
        {% endif %}
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    {% endfor %}
"""


def generate_flask_files(config):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.from_string(flask_blueprint_template)

    for module_name, details in config['flask']['blueprints'].items():
        for class_description, class_details in details.items():
            module_path = os.path.join('..', class_details['module'].replace('.', '/'))
            directory, file_name = os.path.split(module_path)
            if not os.path.isdir(directory):
                os.makedirs(directory, exist_ok=True)
            full_file_path = os.path.join(directory, file_name + '.py')

            methods = {}
            for route, endpoint_list in class_details['routes'].items():
                for endpoint in endpoint_list:
                    for http_method in endpoint['methods']:
                        method_name = http_method.lower()
                        if method_name not in methods:
                            methods[method_name] = {
                                "arg_list": "",
                                "arg_details": ""
                            }
                        # Extract arguments from the route
                        arg_names = []
                        for part in route.split('/'):
                            if part.startswith('<') and part.endswith('>'):
                                arg_type, arg_name = part[1:-1].split(':')
                                arg_names.append(arg_name)
                        # Update the method details with arguments
                        # Default all args after the first to None
                        default_args = [f"{arg}=None" if i != 0 else arg for i, arg in enumerate(arg_names)]
                        methods[method_name]["arg_list"] = ", ".join(default_args)

                        # Generate optional arg handling logic
                        if len(arg_names) > 1:
                            optional_arg_details = "if " + " and ".join([f"{arg} is not None" for arg in arg_names[1:]])
                            optional_arg_details += ":\n            # Handle case where all optional args are provided\n            pass\n        else:\n            # Handle case where some or no optional args are provided\n            pass"
                            methods[method_name]["arg_details"] = optional_arg_details

            with open(full_file_path, 'w', encoding='utf-8') as f:
                f.write(template.render(class_name=class_details['class'], methods=methods))


generate_flask_files(config_json)
