# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午9:20
# @Author  : 魏洪志
# @File    : 12.函数之间存在隔离性.py
# @Software: PyCharm

"""
在函数内部所定义的变量是具有隔离性的
    局部变量
"""

# def test_1():
#     num_1 = 10
#     print(num_1)

# 无法调用函数1中的变量
# def test_2():
#     print(num_1)


"""
如果定义多个函数一起使用同一个变量, 则需要定义全局变量
"""

num_2 = 20


def test_1():
    print(num_2)


def test_2():
    print(num_2)


test_1()
test_2()
