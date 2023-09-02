# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午9:45
# @Author  : 魏洪志
# @File    : 15.将函数引用作为一个参数进行传递.py
# @Software: PyCharm


def test_1():
    print(1)


def test_2():
    print(2)
    return test_1


func_obj = test_2()


def test_3(obj):
    print(3)
    print(id(func_obj))
    print(id(obj))
    obj()


test_3(func_obj)


"""
1. test_2函数返回的是test_1的地址
2. 使用func_obj变量将test_2的返回值接收, func_obj存储的是test_1的地址
3. 调用test_3, 并将func_obj这个变量传递给了test_3的形参: obj, 当前的obj存储的是test_1
4. 在test_3中调用了obj, 就相当于在test_3中调用了test_1()
"""


# 装饰器最主要的作用是在不修改原有代码的情况下可以动态添加当前函数的功能
