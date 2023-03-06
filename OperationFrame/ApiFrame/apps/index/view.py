# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/03
"""
import typing as t

from OperationFrame.ApiFrame.base import app


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: t.Union[str, None] = None):
    return {"item_id": item_id, "q": q}
