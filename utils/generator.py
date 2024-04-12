import os
import textwrap
from jinja2 import Environment, FileSystemLoader
from config import ConfigUtil

flask_template = """
# -*- coding: UTF-8 -*-
from flask.views import MethodView
from utils.response.R import R
from utils.response.enums import Code
from utils.response.msg_enum import SUCCESS_MSG
from utils.error.decorated_error import handle_exceptions
\n
class {{ class_name }}(MethodView):
    {% for method_func, method_detail in methods.items() %}
    @handle_exceptions
    def {{ method_func }}(self{% if method_detail.arg_list %}, {{ method_detail.arg_list }}{% endif %}):
        {% if method_detail.arg_details %}
        {{ method_detail.arg_details|trim }}
        {% else %}
        # Write the implementation details here
        {% endif %}
        return R().code(Code.SUCCESS).msg(SUCCESS_MSG).data({}).build()
    {% endfor %}
"""
config_json = ConfigUtil().get_config()


def extract_args(route):
    """
    从路由字符串中提取参数名。

    参数：
    - route: 字符串，表示一个URL路由，其中参数使用尖括号（<>）包裹。

    返回值：
    - list: 包含所有参数名的列表，参数名是从路由中提取的，不包含尖括号。

    示例：
    - 对于路由字符串`'/users/<int:user_id>/posts/<str:post_title>'`，
      将返回`['user_id', 'post_title']`。
    """
    # 使用列表推导式从路由中提取参数名
    return [part[1:-1].split(':')[1] for part in route.split('/') if part.startswith('<') and part.endswith('>')]


def generate_optional_arg_details(arg_names):
    """
    生成关于可选参数的细节描述。

    参数:
    arg_names: 一个包含参数名的列表，这些参数可能是可选的。

    返回值:
    根据提供的参数名列表，生成一个条件判断结构的字符串，用于检查除第一个参数外的其他参数是否为None。
    如果参数列表长度小于等于1，返回空字符串。
    """
    if len(arg_names) <= 1:
        return ""

    # 构建条件字符串，检查每个参数是否不为None
    conditions = " and ".join(f"{arg} is not None" for arg in arg_names[1:])

    # 定义一个无缩进的多行字符串模板，用于构建条件判断的框架
    no_indent_template = """\
if {conditions}:
    pass
else:
    pass"""

    # 将条件字符串插入到模板中
    no_indent_result = no_indent_template.format(conditions=conditions)

    # 使用textwrap.indent为最终结果增加缩进
    result = textwrap.indent(no_indent_result, '        ')
    return result


def generate_flask_files(config):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.from_string(flask_template)

    # 初始化计数器
    files_generated = 0
    files_skipped = 0

    # 初始化列表用于存储文件路径
    skipped_files_list = []
    generated_files_list = []

    for module_name, details in config['flask']['blueprints'].items():
        for class_description, class_details in details.items():
            module_path = os.path.join('..', class_details['module'].replace('.', '/'))
            directory, file_name = os.path.split(module_path)
            os.makedirs(directory, exist_ok=True)
            full_file_path = os.path.join(directory, file_name + '.py')

            if os.path.isfile(full_file_path):
                print(f"文件已存在，已略过: {full_file_path}")
                files_skipped += 1
                skipped_files_list.append(full_file_path)
                continue

            methods = {}
            for route, endpoint_list in class_details['routes'].items():
                for endpoint in endpoint_list:
                    for http_method in endpoint['methods']:
                        method_name = http_method.lower()
                        if method_name not in methods:
                            methods[method_name] = {"arg_list": "", "arg_details": ""}

                        arg_names = extract_args(route)
                        default_args = [f"{arg}=None" if i != 0 else arg for i, arg in enumerate(arg_names)]
                        methods[method_name]["arg_list"] = ", ".join(default_args)
                        methods[method_name]["arg_details"] = generate_optional_arg_details(arg_names)

            with open(full_file_path, 'w', encoding='utf-8') as f:
                f.write(template.render(class_name=class_details['class'], methods=methods))
                files_generated += 1
                generated_files_list.append(full_file_path)

    # 打印统计信息
    print(f"生成文件个数：{files_generated}")
    print("生成的文件列表：")
    for file_path in generated_files_list:
        print(file_path)

    print(f"跳过文件个数：{files_skipped}")
    print("跳过的文件列表：")
    for file_path in skipped_files_list:
        print(file_path)


generate_flask_files(config_json)
