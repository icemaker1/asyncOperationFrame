# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/18
"""
import sys
import asyncio
from OperationFrame.menu import menu_enter


if __name__ == '__main__':
    asyncio.run(menu_enter(sys.argv))
