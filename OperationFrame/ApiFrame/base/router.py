# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/03
"""
from fastapi import APIRouter as BaseAPIRouter

Routers = []


class APIRouter(BaseAPIRouter):
    def __init__(self, *args, **kwargs):
        super(APIRouter, self).__init__(*args, **kwargs)
        Routers.append(self)


route_auth = APIRouter(prefix="/auth", tags=["auth"])
