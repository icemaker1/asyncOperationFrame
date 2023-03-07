# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/08/03
"""
from OperationFrame.ApiFrame.base import app, Middleware, Routers
from OperationFrame.config import config
from OperationFrame.utils.logger import logger
from OperationFrame.lib.tools import import_paths


# 载入模块
for module, view_dir in config.API_VIEWS_DIR.items():
    import_paths(view_dir)
    logger.debug(f"import models {module}: {config.FRAME_NAME}.{view_dir}")

# 载入路由
for route in Routers:
    app.include_router(route)
    logger.debug(f"include router: {route.prefix}")

# 载入中间件
for name, middleware in Middleware[::-1]:
    app.add_middleware(middleware)
    logger.debug(f"add middleware: {name}")
