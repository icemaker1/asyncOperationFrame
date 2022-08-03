# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/19
"""
from OperationFrame.config.config import BaseConfig
from OperationFrame.config.config_env import EnvConfig
from OperationFrame.config.config_service import ServiceConfig


config = BaseConfig()
config.extend(EnvConfig)
config.extend(ServiceConfig)

__all__ = ['config']
