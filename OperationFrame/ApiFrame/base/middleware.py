# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/03
"""
from time import time
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from starlette.types import ASGIApp
from werkzeug import Request

from OperationFrame.config import config
from OperationFrame.utils.logger import logger


Middleware = []


def add_wrapper(cls):
    def wrapper(*args, **kwargs):
        return cls(*args, **kwargs)

    if getattr(cls, 'using', True):
        Middleware.append((getattr(cls, 'name', None) or cls.__name__, cls))
    return wrapper


@add_wrapper
class TraceMiddleware(BaseHTTPMiddleware):
    """ 添加回溯信息 """
    app: ASGIApp
    name: str = 'trace'

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        before = time()
        trace_data = {
            'Ts-Request-Id': request.headers.get('Ts-Request-Id', str(uuid4())),
        }
        with logger.contextualize(**trace_data):
            response: Response = await call_next(request)
        after = time()
        response.headers.update({
            'X-Request-After': str(after),
            'X-Request-Before': str(before),
            'X-Response-Time': str(after - before),
            **trace_data
        })
        return response


@add_wrapper
class VerifyMiddleware(BaseHTTPMiddleware):
    """ 校验方式：加密校验 """
    app: ASGIApp
    name: str = 'verify'
    using: bool = config.VERIFY_TYPE_KEY

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        print('sign', request.headers.get('sign', ''))
        print('time', request.headers.get('time', ''))
        response: Response = await call_next(request)
        return response
