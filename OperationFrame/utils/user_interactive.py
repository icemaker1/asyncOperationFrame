# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/21
"""
import typing as t


def ask_input(msg: t.AnyStr) -> t.AnyStr:
    """
    获取用户输入
    """
    return input(f"\033[32mASK\033[0m    --    {msg}:").strip()


def ask_yesno(msg: t.AnyStr) -> t.AnyStr:
    """
    获取用户输入回答，[yes/no]
    """
    while True:
        value = input(f"\033[32mASK\033[0m    --    {msg} [yes/no]:").strip()
        if value.lower() in ['yes', 'no']:
            return value.lower()
