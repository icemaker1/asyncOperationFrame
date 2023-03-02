# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/01
"""
import typing as t
from .triggers import ErrorHandler


class Middleware(ErrorHandler):
    def __init__(self, func: t.Callable):
        self.func = func

    async def __call__(self, *args, **kwargs):
        with self.menu_handler():
            await self.func(*args, **kwargs)
