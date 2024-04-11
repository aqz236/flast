## Flast

**这是一个基于 [Flask](https://github.com/pallets/flask) 构建的超轻量级，用于构建 Web 应用程序的 Python 脚手架，强调配置大于编码的哲学。
整个脚手架大小仅26KB，通过配置`config.yaml`文件以生成路由，只需简单地配置，配合内置的代码生成器，自动化生成业务代码。
**



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
  host: "0.0.0.0"
  port: 5222
  baseApi: "/song"
  blueprints:
    test:
      TestManager:
        module: "api.test"
        class: "TestManager"
        routes:
          "/test":
            - endpoint: "create_task"
              methods:
                - "POST"
          "/test/<int:obj>":
            - endpoint: "get_task_info | delete_task | update_task"
              methods:
                - "GET"
                - "DELETE"
                - "PUT"
          "/test/<int:obj>/<string:action>":
            - endpoint: "task_action"
              methods:
                - "GET"
```

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2013-present, aqz236
