# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
from OperationFrame.utils.cbvmenu import MenuMetaClass, BaseMeta


class CommonCbv(metaclass=MenuMetaClass):
    Meta = BaseMeta

    @property
    def meta_params(self):
        return getattr(self.Meta, 'params', 'None')
