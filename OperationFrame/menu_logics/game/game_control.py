# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/19
"""
from OperationFrame.utils.logger import logger
from OperationFrame.utils.connecter import remote


async def start(srv_id):
    cmd = f''
    remote_res = await remote(cmd, 'ip')
    if remote_res:
        logger.info(f'{srv_id} 启动成功')
        return True
    else:
        logger.error(f'{srv_id} 启动失败, 原因: {remote_res}')
        return remote_res


async def stop(srv_id):
    cmd = f''
    remote_res = await remote(cmd, 'ip')
    if remote_res:
        logger.info(f'{srv_id} 关闭成功')
        return True
    else:
        logger.error(f'{srv_id} 关闭失败, 原因: {remote_res}')
        return remote_res
