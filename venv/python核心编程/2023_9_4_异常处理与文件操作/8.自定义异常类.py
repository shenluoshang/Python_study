# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午8:56
# @Author  : 顾安
# @File    : 8.自定义异常类.py
# @Software: PyCharm


"""
现在想要实现一个用户登录功能
    用户在输入密码时如果密码错误直接抛出密码错误的异常
"""


class PassWordError(Exception):
    def __str__(self):
        return '密码错误...'

    # 作用于交互环境的
    def __repr__(self):
        return '密码错误...'


name = input('请输入用户名: ')
password = input('请输入密码: ')

local_name = '安娜'
local_password = 'admin'

try:
    if name != local_name or password != local_password:
        raise PassWordError
except PassWordError as e:
    print(e)

