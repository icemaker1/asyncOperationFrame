## OperationFrame

> 这是一个基于 Python 3.10+ 的 异步运维框架, 提供菜单终端与业务接口的执行任务方式
>
> 分离终端执行与api执行方式，集中两者的业务接口
>
> ApiFrame 是一个 fastapi 的快速开发脚手架，提供普通接口与异步任务、定时任务功能(未完成)

### 相关包

- asyncssh = 2.11.0
- tortoise-orm[asyncmy] = 0.19.2
- fastapi = 0.79.0
- uvicorn = 0.18.2

### 启动服务

> python3 main.py Action [options]

### 关于 orm

> 协程服务中不建议使用同步组件
