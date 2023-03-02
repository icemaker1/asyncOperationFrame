# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/01
"""
import contextlib
import typing as t
from .event import menu
from .error_classify import MenuLostError, MenuParamError


class ErrorHandler:
    help_error: t.Tuple[any] = (
        MenuLostError,
        MenuParamError
    )
    help_message: t.AnyStr = "usage: ./main.py Action [options]\n\nSupport Actions:\n"

    def _menu_help(self):
        help_message = self.help_message
        for task in menu.tasks:
            format_param = str([menu.tasks.get(task)['params']]).replace("'", "")
            help_message += f"    {task:<26}   {format_param:>20}  {menu.tasks.get(task)['name']}\n"
        print(help_message)

    @contextlib.contextmanager
    def menu_handler(self):
        try:
            yield
        except BaseException as err:
            if isinstance(err, self.help_error):
                self._menu_help()
                err_message = err.__str__()
            elif isinstance(err, KeyboardInterrupt):
                err_message = f'取消执行菜单'
            else:
                err_message = '未定义的错误'

            print(f"{err_message} | 错误类型: {type(err)} | 错误信息: {err.__str__()}")
