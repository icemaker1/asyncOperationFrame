# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
import os
from importlib import import_module

from OperationFrame.config import config


def import_paths(module: str):
    """
    module 模块 name
    导入 module 下的资源
    """
    for path, _, files in os.walk(f'{config.PROJECT_PATH}/{module}'):
        for file in files:
            if not path.split('/')[-1].startswith('_') or path.split('/')[-1] == '__init__':
                import_module(
                    f"{config.FRAME_NAME}{path.split(str(config.PROJECT_PATH))[1].replace('/', '.')}.{file.split('.')[0]}"
                )
