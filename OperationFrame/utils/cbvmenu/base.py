# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
import asyncio
import typing as t


def _get_attr(mcs, key):
    meta: BaseMeta = getattr(mcs, 'Meta', None)
    return getattr(meta if hasattr(meta, key) else BaseMeta, key)


class BaseMeta:
    name: str = '未定义'
    sign: str = None
    params: str = None
    func: t.Union[t.List, t.Callable, t.Awaitable] = None


class MenuMetaClass(type):
    def __new__(mcs, cls_name, bases, attrs):
        mcs = type.__new__(mcs, cls_name, bases, attrs)

        name = _get_attr(mcs, 'name')
        sign = _get_attr(mcs, 'sign')
        params = mcs().meta_params

        if name and sign:
            menu.tasks[sign] = {'name': name, 'mcs': mcs, 'params': params}

        return mcs


class MenuManager:

    def __init__(
            self,
            on_startup: t.Sequence[t.Callable] = None,
            on_shutdown: t.Sequence[t.Callable] = None,
    ):
        self.tasks: t.Dict[t.Dict, t.Union[str, t.TypeVar]] = {}
        self.on_startup = [] if on_startup is None else list(on_startup)
        self.on_shutdown = [] if on_shutdown is None else list(on_shutdown)
        self.lifespan_context: t.Callable = _DefaultLifespan(self)

    def add_event_handler(self, event_type: str, func: t.Callable) -> None:
        assert event_type in ("startup", "shutdown")

        if event_type == "startup":
            self.on_startup.append(func)
        else:
            self.on_shutdown.append(func)

    def on_event(self, event_type: str) -> t.Callable:
        """
        注册的事件串行而不异步
        """
        def decorator(func: t.Callable) -> t.Callable:
            self.add_event_handler(event_type, func)
            return func

        return decorator

    async def startup(self) -> None:
        for handler in self.on_startup:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()

    async def shutdown(self) -> None:
        for handler in self.on_shutdown:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()


class _DefaultLifespan:
    def __init__(self, manager: MenuManager):
        self.manager = manager

    async def __aenter__(self) -> None:
        await self.manager.startup()

    async def __aexit__(self, *exc_info: object) -> None:
        await self.manager.shutdown()

    def __call__(self: t.TypeVar) -> t.TypeVar:
        return self


menu = MenuManager()
