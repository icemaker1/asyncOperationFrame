# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
from OperationFrame.lib.scheduler import AsyncScheduler
from OperationFrame.utils.cbvmenu import MenuMetaClass, BaseMeta
from OperationFrame.utils.user_interactive import ask_yesno


class GameCbv(metaclass=MenuMetaClass):
    Meta = BaseMeta

    @property
    def meta_params(self):
        return getattr(self.Meta, 'params', '*srv_id')

    @staticmethod
    async def _run_task(mcs_method, games: list):
        scheduler = AsyncScheduler()
        for game in games:
            scheduler.create_task(mcs_method(game))
        await scheduler.join()

    async def run(self, *games):
        if not games:
            # 这里询问游戏服
            games = ['private_726', 'private_727']

        print(games)
        if not ask_yesno(f'是否对上述游戏服执行 {self.Meta.name} 任务'):
            return False

        if isinstance(self.Meta.func, list):
            for method in self.Meta.func:
                await self._run_task(method, games)
        else:
            await self._run_task(self.Meta.func, games)
