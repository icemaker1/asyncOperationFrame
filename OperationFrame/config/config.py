# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/19
"""
from pathlib import Path
from typing import Any


class BaseConfig:
    """
    config 基础配置
    """
    PROJECT_PATH:      Path = Path(__file__).parent.parent.resolve()   # 项目根目录
    FRAME_NAME:         str = PROJECT_PATH.name                        # 框架名称
    TERMINAL_VIEW_DIR: list = ['menu_terminal']                        # 终端菜单视图目录
    API_VIEW_DIR:      list = ['menu_api']                             # 接口菜单视图目录
    DB_MODELS:         list = ['OperationFrame.model']                 # orm模型列表

    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __getitem__(self, item) -> Any:
        return getattr(self, item)

    def get(self, item, default=None) -> Any:
        return getattr(self, item, default)

    def extend(self, cls) -> None:
        for key in dir(cls):
            if key == key.upper():
                self[key] = getattr(cls(), key)
