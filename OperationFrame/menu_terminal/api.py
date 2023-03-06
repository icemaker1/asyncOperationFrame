# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/08/03
"""
from uvicorn import run
from OperationFrame.config import config
from OperationFrame.utils.cbvmenu import CommonCbv


class ApiStart(CommonCbv):
    """
    生产部署请用 gunicorn + uvicorn 部署
    这里仅仅提供前台启动方式
    """

    def run(self, debug=None):
        run(
            app='OperationFrame.ApiFrame.rule:app', host=config.API_HOST,
            port=config.API_PORT, debug=config.API_DEBUG, reload=config.API_RELOAD
        )

    class Meta:
        name = 'api启动'
        sign = 'api_start'
        params = 'debug/None'


class ApiStop(CommonCbv):

    async def run(self):
        pass

    class Meta:
        name = 'api关闭'
        sign = 'api_stop'


class ApiRestart(CommonCbv):

    async def run(self):
        pass

    class Meta:
        name = 'api重启'
        sign = 'api_restart'
