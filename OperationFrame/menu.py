# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/19
"""
import asyncio
import typing as t

from OperationFrame.config import config
from OperationFrame.lib.tools import import_paths
from OperationFrame.utils.cbvmenu import menu
from OperationFrame.utils.globalMiddlewares import Middleware, MenuLostError, MenuParamError
from OperationFrame.utils.logger import logger


# 载入菜单模块
for module in config.TERMINAL_VIEW_DIR + config.API_VIEW_DIR:
    import_paths(module)


@Middleware
@logger.catch(exclude=(MenuLostError, MenuParamError))
async def menu_enter(argv: t.List) -> t.NoReturn:
    async with menu.lifespan_context():
        param_num = len(argv)
        if param_num <= 1:
            raise MenuLostError
        task = menu.tasks.get(argv[1], None)
        if not task:
            raise MenuLostError

        param = task['params']
        if param == 'None' or '*' in param:
            if param == 'None' and param_num != 2 or '*' in param and param_num < 3:
                raise MenuParamError
        elif '/' in param:
            if param_num not in [2, 3]:
                raise MenuParamError
        else:
            if param_num != 3:
                raise MenuParamError

        self = task['mcs']()
        if asyncio.iscoroutinefunction(self.run):
            await self.run(*argv[2:])
        else:
            self.run(*argv[2:])
