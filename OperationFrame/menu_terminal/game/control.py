# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/20
"""
from OperationFrame.utils.cbvmenu import GameCbv
from OperationFrame.menu_logics.game.game_control import start, stop


class GameStart(GameCbv):

    class Meta:
        name = '游戏服启动'
        sign = 'game_start'
        func = start


class GameStop(GameCbv):

    class Meta:
        name = '游戏服关闭'
        sign = 'game_stop'
        func = stop


class GameRestart(GameCbv):

    class Meta:
        name = '游戏服重启'
        sign = 'game_restart'
        func = [stop, start]
