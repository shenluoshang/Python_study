# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午9:16
# @Author  : 魏洪志
# @File    : 11.自定义函数类型.py
# @Software: PyCharm


"""
自定义函数有四种类型
    1.无参数无返回值
    2.无参数有返回值
    3.有参数无返回值
    4.有参数有返回值
"""


def test_1():
    print('无参数无返回值')


def test_2():
    return '无参数有返回值'


def test_3(num):
     print('有参数无返回值:', num)


def test_4(num):
    return f'有参数无返回值:{num}'

