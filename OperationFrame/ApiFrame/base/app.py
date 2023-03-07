# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/08/03
"""
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from OperationFrame.config import config

app = FastAPI()

register_tortoise(
    app,
    db_url=f'mysql://{config.MYSQL_USER}:{config.MYSQL_PASS}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DB}',
    modules={'models': config.DB_MODELS}
)
