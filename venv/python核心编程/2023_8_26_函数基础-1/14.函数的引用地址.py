# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午9:35
# @Author  : 魏洪志
# @File    : 14.函数的引用地址.py
# @Software: PyCharm


def test_1():
    print(1)


def test_2():
    print(2)


# 获取函数本身的地址不能在函数名称后加()
print(id(test_1))
print(id(test_2))

# 将test_2的引用地址给了test_1
test_1 = test_2

test_1()

"""
将函数引用作为参数传递给另外一个函数的案例
"""


def test_3():
    print('函数3')


def test_4(func_obj):
    func_obj()
    print('函数4')


func_addr = test_3
test_4(func_addr)


# 将一个函数的地址进行return
def test_5():
    print(1)
    return test_4


func_obj_attr = test_5()
func_obj_attr(test_3)



