# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午9:32
# @Author  : 魏洪志
# @File    : 13.函数的嵌套调用.py
# @Software: PyCharm


def test_1():
    print('函数名: test_1')
    print('这是函数1需要运行的代码...')
    print('函数1即将退出...')


def test_2():
    print('函数名: test_2')
    test_1()
    print('函数2即将退出...')


test_2()

