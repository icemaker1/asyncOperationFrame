# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2023/03/01
"""
import typing as t


class MenuBaseError(Exception):
    message: t.AnyStr

    def __str__(self):
        return self.message


class MenuLostError(MenuBaseError):
    message: t.AnyStr = '未被定义的菜单模块'


class MenuParamError(MenuBaseError):
    message: t.AnyStr = '参数错误的菜单模块'
