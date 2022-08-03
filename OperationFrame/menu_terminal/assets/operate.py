# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/26
"""
from OperationFrame.model import Game
from OperationFrame.utils.cbvmenu import CommonCbv


class AssetsShowStatus(CommonCbv):

    async def run(self):
        res = await Game.all()
        print(res)

    class Meta:
        name = '项目资产详情'
        sign = 'assets_show_status'
