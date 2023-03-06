# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
import os
import sys
from importlib import import_module

from OperationFrame.config import config


_platform = sys.platform


def import_paths(module: str):
    """
    module 模块 name
    递归导入 module 下的资源
    """
    platform_dir = f'{config.PROJECT_PATH}.{module}'
    platform_dir = platform_dir.replace('.', '/') if _platform == 'linux' else platform_dir.replace('.', '\\')

    for path, _, files in os.walk(platform_dir):
        for file in files:
            _path = path.split(str(config.PROJECT_PATH))[1].replace('/', '.').replace('\\', '.')
            _path = f"{config.FRAME_NAME}{_path}"
            if not _path.split('.')[-1].startswith('_') or path.split('.')[-1] == '__init__':
                import_module(f"{_path}.{file.split('.')[0]}")
