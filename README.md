## Flast

**这是一个基于 [Flask](https://github.com/pallets/flask) 构建的超轻量级，用于构建 Web 应用程序的 Python 脚手架，封装灵感来自Spring的配置文件，强调配置大于编码的哲学。
整个脚手架大小仅26KB，通过配置`config.yaml`文件以生成路由，只需简单地配置，配合内置的代码生成器，自动化生成业务代码、自动注册路由。**




<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="300" src="https://github.com/vuejs/vue/assets/54022108/3ef1fb58-e697-4272-b839-6645c0f4d68a" alt="Vue logo"></a></p>

<p align="center">
  <a href="https://pypi.org/project/flast/"><img src="https://img.shields.io/pypi/v/flast.svg?sanitize=true" alt="Python Package Index"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8%20|%203.9-blue.svg?sanitize=true" alt="Python Version"></a>
  <a href="https://github.com/aqz236/flast/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg?sanitize=true" alt="License MIT"></a>
  <a href="https://github.com/aqz236/flast/discussions"><img src="https://img.shields.io/badge/chat-on%20github-7289da.svg?sanitize=true" alt="Chat"></a>
</p>

## 特性

- **极度轻量**：整个脚手架仅有26KB
- **配置大于编码**：只需简单配置`config.yaml`，即可生成业务代码
- **封装有链式返回值**：方便链式操作
- **异常处理**：内置异常处理机制
- **专用的代码生成器**：自动化生成业务代码

## 如何开始
1. 克隆本项目至本地。

```bash
git clone https://github.com/aqz236/flast
```
2. 切换到项目文件夹
```bash
cd flast
```
3. 安装依赖
```bash
pip install -r requirements.txt
```
4. 修改`config.yaml`至你需要的路由设置
5. 手动运行utils/generator.py，根据配置生成业务代码


---

## 配置说明


`config.yaml`主要配置项目路由和一些其他信息。下面是一个示例，供理解参考。

```yaml
flask:
  host: 0.0.0.0          # 运行Flask服务的主机地址，0.0.0.0代表监听所有公开的IP地址
  port: 5222             # 运行Flask服务的端口号
  baseApi: /song         # API的基础路径，所有蓝图的路由都将以此路径作为前缀

  # `blueprints`节定义了多个蓝图，用于组织不同的路由群组
  blueprints:
    # 自定义蓝图名称
    example_name:
      # 在此下定义test1蓝图相关的类与路由信息
      TestManager:               # TestManager为这部分配置的索引名，是蓝图中的一个组件
        module: api.test1        # 定义TestManager类所在的模块路径，'.' 表示层级关系
        class: Test1Manager      # 定义TestManager类的类名
        routes:                  # 定义该类关联的路由和方法
          # 定义一个路由地址以及支持的方法
          /test:
            - endpoint: create_task    # 定义endpoint名称，同蓝图下不允许重名
              methods:                # 列出支处理的HTTP方法
                - POST
          # 定义带参数的路由，参数由尖括号<>包围
          # `/song/test/<obj>/<name>`请求时将解析参数至对应的处理函数
          /test/<int:obj>/<string:name>:
            - endpoint: get_task_info
              methods:              # 列出支持的方法
                - GET
                - DELETE
                - PUT
          # 类似的，还可以定义其他路由和处理函数关联
          /test/<int:obj>/<string:action>:
            - endpoint: task_action
              methods:
                - GET

    # test2 蓝图定义开始
    test2:
      TestManager:                    # TestManager为这部分配置的索引名
        module: api.test2             # 定义TestManager类所在的模块路径
        class: Test2Manager           # 定义TestManager类的类名
        routes:                       # 定义该类关联的路由和方法
          /test2:
            - endpoint: create_task
              methods:                # 列出支处理的HTTP方法，支持多种方法
                - POST
                - GET
                - PUT
                - DELETE
                - PATCH
                - HEAD
                - OPTIONS
```

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2024-present, aqz236
