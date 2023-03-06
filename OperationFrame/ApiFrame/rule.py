# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/08/03
"""
from fastapi import Request

from OperationFrame.config import config
from OperationFrame.utils.logger import logger
from OperationFrame.lib.tools import import_paths
from OperationFrame.ApiFrame.base import app


# 载入模块
for module, view_dir in config.API_VIEWS_DIR.items():
    import_paths(view_dir)
    logger.debug(f"import models {module}: {config.FRAME_NAME}.{view_dir}")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    print('response', response)
    print('request', request)
    print(app.user_middleware)
    return response

