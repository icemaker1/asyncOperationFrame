# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/08/03
"""
from typing import Union

from OperationFrame.ApiFrame.base import app
from OperationFrame.model import Game


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/orm")
async def read_orm():
    res = await Game.all()
    print(res)
    return {"names": 'lhl'}
