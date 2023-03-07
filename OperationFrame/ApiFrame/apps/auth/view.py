# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/07
"""
from OperationFrame.ApiFrame.base import route_auth


@route_auth.get("/", summary='仅测试的根路由')
async def auth_test():
    return {'message': '认证根路由'}
