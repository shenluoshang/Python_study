# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午8:52
# @Author  : 魏洪志
# @File    : 6.函数引用.py
# @Software: PyCharm


def test_1():
    print('我是函数1')


def test_2():
    print('我是函数2')


test_1 = test_2

test_1()


# 闭包
def test(num):
    def wrapper():
        print(num)
    return wrapper


# def my_func(func_obj):
#     def wrapper(name):
#         print('我是一个闭包...')
#         func_obj(name)
#     return wrapper
#
#
# @my_func  # 语法糖
# def print_name(name):
#     print('打印信息: ', name)
#
#
# print_name('安娜')
