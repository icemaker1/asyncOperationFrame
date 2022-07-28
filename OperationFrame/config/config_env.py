# _*_ coding: utf-8 _*_
"""
Author: 'LingLing'
Date: 2022/07/28
"""
import os


class DEV:
    """
    开发环境配置
    """
    ENV:                str = 'DEV'                                   # 当前环境
    MYSQL_DB:           str = 'db_name'                               # 开发环境: 管理机数据库名称
    MYSQL_HOST:         str = '127.0.0.1'                             # 开发环境: 管理机数据库主机
    MYSQL_PORT:         int = 3306                                    # 开发环境: 管理机数据库端口
    MYSQL_USER:         str = 'root'                                  # 开发环境: 管理机数据库用户
    MYSQL_PASS:         str = 'db_pass'                               # 开发环境: 管理机数据库密码
    MYSQL_CHAR:         str = 'utf8'                                  # 开发环境: 管理机数据库编码


class TEST:
    """
    测试环境配置
    """
    ENV:                str = 'TEST'                                  # 当前环境
    MYSQL_DB:           str = 'db_name'                               # 测试环境: 管理机数据库名称
    MYSQL_HOST:         str = '127.0.0.1'                             # 测试环境: 管理机数据库主机
    MYSQL_PORT:         int = 3306                                    # 测试环境: 管理机数据库端口
    MYSQL_USER:         str = 'root'                                  # 测试环境: 管理机数据库用户
    MYSQL_PASS:         str = 'db_pass'                               # 测试环境: 管理机数据库密码
    MYSQL_CHAR:         str = 'utf8'                                  # 测试环境: 管理机数据库编码


class PROD:
    """
    生产环境配置
    """
    ENV:                str = 'PROD'                                  # 当前环境
    MYSQL_DB:           str = 'db_name'                               # 生产环境: 管理机数据库名称
    MYSQL_HOST:         str = '127.0.0.1'                             # 生产环境: 管理机数据库主机
    MYSQL_PORT:         int = 3306                                    # 生产环境: 管理机数据库端口
    MYSQL_USER:         str = 'root'                                  # 生产环境: 管理机数据库用户
    MYSQL_PASS:         str = 'db_pass'                               # 生产环境: 管理机数据库密码
    MYSQL_CHAR:         str = 'utf8'                                  # 生产环境: 管理机数据库编码


env = os.environ.get('ENVIORNMENT', 'dev')
EnvConfig = (env == "test" and TEST or env == "prod" and PROD or env == "dev" and DEV)
