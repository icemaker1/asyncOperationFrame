# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/01
"""
import time
import datetime
from tortoise import Tortoise
from OperationFrame.config import config
from OperationFrame.utils.cbvmenu import menu


def _real_time() -> datetime.timedelta:
    return datetime.timedelta(seconds=int(str(time.time()).split(".")[0]))


startup = _real_time()


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

