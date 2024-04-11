# utils/route_manager.py
import importlib
from flask import Blueprint
from utils.config import ConfigUtil as c
import inspect

# 读取config.json中所有的api配置
config = c().get_config()
blueprints_name_list = list(config["flask"]['blueprints'].keys())


class RouteManager:
    def __init__(self, app):
        """
        类的初始化方法。

        :param app: 传入的应用对象，用于将当前对象注册为该应用的一个组件。
        """
        self.blueprint = None
        # 将当前对象注册到传入的应用app中，完成初始化过程。
        self.register_to_app(app)

    def register_routes_from_config(self, blueprint_name):
        """
        从配置文件中注册路由到指定的蓝图。

        :param blueprint_name: 蓝图的名称，用于从配置中获取对应的路由配置。
        """
        # 基础API路径来自于配置文件
        base_api = config["flask"]["baseApi"]
        # 获取指定蓝图的配置信息
        api_config = config["flask"]["blueprints"][blueprint_name]

        # 遍历配置，动态加载并注册路由
        for item in api_config.values():
            module_path = item.get('module')
            class_name = item.get('class')
            routes = item.get('routes')

            # 检查必须的配置项是否提供
            if module_path is None or class_name is None:
                raise ValueError('Both module path and class names must be provided in the configuration.')

            # 动态导入模块
            view_module = importlib.import_module(module_path)
            # 在模块中寻找对应的类
            view_cls = self.find_class_in_module(view_module, class_name)

            if view_cls is None:
                raise AttributeError(f"Could not find class {class_name} in module {module_path}.")

            # 遍历并注册每个路由规则
            for rule, endpoints in routes.items():
                for endpoint_info in endpoints:
                    endpoint = endpoint_info['endpoint']
                    methods = endpoint_info['methods']
                    # 添加URL规则到蓝图
                    self.blueprint.add_url_rule(
                        base_api + rule,
                        endpoint=endpoint,
                        view_func=view_cls.as_view(endpoint),
                        methods=methods
                    )

    @staticmethod
    def find_class_in_module(module, class_name):
        """
        在指定模块中查找指定名称的类。

        参数:
        - module: 要搜索的模块对象。
        - class_name: 要查找的类名（不区分大小写）。

        返回值:
        - 如果找到匹配的类，则返回类对象；否则返回None。
        """
        # 遍历模块中所有成员，筛选出类，并检查其名称是否匹配
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if name.lower() == class_name.lower():
                return obj  # 找到匹配的类，返回该类对象
        return None  # 未找到匹配的类，返回None

    def set_route(self, *views):
        pass

    def register_to_app(self, app):
        """
        将当前实例中的路由蓝图注册到指定的应用程序中。

        :param app: Flask应用程序实例，用于注册蓝图。
        """
        for blueprint_name in blueprints_name_list:  # 遍历蓝图名称列表
            self.blueprint = blueprint = Blueprint(blueprint_name, __name__)  # 创建并赋值蓝图实例
            self.register_routes_from_config(blueprint_name)  # 根据配置注册路由
            app.register_blueprint(blueprint)  # 将蓝图注册到Flask应用
