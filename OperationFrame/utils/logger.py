# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/29
"""
import sys
import contextvars
from loguru import _defaults
from loguru._logger import Logger as BaseLogger, Core

_defaults.LOGURU_INFO_COLOR = "<green>"
_defaults.LOGURU_ERROR_COLOR = "<red><bold><blink>"
_defaults.LOGURU_WARNING_COLOR = "<yellow><bold>"
_defaults.LOGURU_CRITICAL_COLOR = "<red><bold>"
filter_context = contextvars.ContextVar("filter_context", default="")


class Logger(BaseLogger):
    ...


logger = Logger(Core(), None, 0, False, False, False, False, True, None, {})
logger.add(sys.stdout, format="<lvl>{level}</lvl> {message}", level="DEBUG", colorize=True)
