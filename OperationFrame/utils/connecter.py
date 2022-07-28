# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/19
"""
import typing as t
import asyncssh
import asyncio

from OperationFrame.config import config


async def result_shell(cmd: str) -> t.Optional[str]:
    """
    本地执行 shell 返回结果
    """
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()

    return stdout.decode()


async def real_shell(cmd: str) -> t.Optional[bool]:
    """
    本地执行 shell 分片结果
    """
    pass


async def remote(cmd: str, host: str) -> t.Optional[str]:
    """
    远程执行 shell 返回结果
    """
    async with asyncssh.connect(
            host, port=9022, client_keys=[config.MANAGER_SSH_KEY], passphrase='', known_hosts=None
    ) as conn:
        result = await conn.run(cmd, check=True)

        return result.stdout
