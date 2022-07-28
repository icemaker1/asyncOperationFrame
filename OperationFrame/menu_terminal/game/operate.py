# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/22
"""
from OperationFrame.utils.cbvmenu import GameCbv


class GameShowInfo(GameCbv):

    async def run(self, game):
        print(f'{game}, 后端版本: 1.1.1.1, 前端版本: 0.0.0.0')

    class Meta:
        name = '游戏服详情'
        sign = 'game_show_info'
        params = 'srv_id'
