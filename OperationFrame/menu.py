# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/19
"""
import asyncio
import time
import datetime
from tortoise import Tortoise

from OperationFrame.config import config
from OperationFrame.lib.tools import import_paths
from OperationFrame.utils.cbvmenu import menu
from OperationFrame.utils.context_manager import menu_handler


# 载入菜单模块
for module in config.TERMINAL_VIEW_DIR + config.API_VIEW_DIR:
    import_paths(module)


# 初始化orm连接
@menu.on_event("startup")
async def init_tortoise():
    await Tortoise.init(
        db_url=f'mysql://{config.MYSQL_USER}:{config.MYSQL_PASS}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DB}',
        modules={'models': config.DB_MODELS}
    )
    # await Tortoise.generate_schemas(safe=True)


@menu.on_event("shutdown")
async def run_time():
    print(f"RunTime: {_real_time() - startup}")


def _real_time():
    return datetime.timedelta(seconds=int(str(time.time()).split(".")[0]))


startup = _real_time()


async def menu_enter(argv):
    async with menu.lifespan_context():
        with menu_handler():
            self = menu.tasks.get(argv[1])['mcs']()
            if asyncio.iscoroutinefunction(self.run):
                await self.run(*argv[2:])
            else:
                self.run(*argv[2:])
