# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
import contextlib

from OperationFrame.utils.cbvmenu import menu


@contextlib.contextmanager
def menu_handler():
    PASS_MENU_ERR = (KeyboardInterrupt, )

    def _menu_help():
        print(f"usage: ./main.py Action [options]\n\nSupport Actions:")
        for task in menu.tasks:
            format_param = str([menu.tasks.get(task)['params']]).replace("'", "")
            print(f"    {task:<26}   {format_param:>20}  {menu.tasks.get(task)['name']}")

    try:
        yield
    except (
        KeyboardInterrupt,
        TypeError,
        IndexError
    ) as err:
        if not isinstance(err, PASS_MENU_ERR):
            _menu_help()

        if isinstance(err, (TypeError, IndexError)):
            err_message = f'参数错误的菜单'
        elif isinstance(err, KeyboardInterrupt):
            err_message = f'取消执行菜单'
        else:
            err_message = '未定义的错误'

        print(f"\n{err_message} | 错误类型: {type(err)} | 错误信息: {err.__str__()}")
        return
