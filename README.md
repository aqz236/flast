# Flast

## 简介

这是一个基于Flask构建的超轻量级脚手架，强调配置大于编码的哲学。
整个脚手架大小仅26KB，通过配置`config.yaml`文件以生成路由，只需简单地配置，配合内置的代码生成器，自动化生成业务代码。

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
