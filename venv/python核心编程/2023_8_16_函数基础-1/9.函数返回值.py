# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午8:52
# @Author  : 魏洪志
# @File    : 9.函数返回值.py
# @Software: PyCharm

"""
函数在计算之后会得出一个结果
    如果我现在想要把这个结果传递给下一个函数进行第二次计算怎么办？
"""


def add_num(num_1, num_2):
    # 把一个结果进行返回
    return num_1 + num_2


res = add_num(5, 10)
print(res)

# 直接打印函数的返回值
print(add_num(7, 12))

"""
没有return的函数情况
    如果一个函数的内部没有写return
        那么解释器会自动加上一段代码: return None
"""


def add_num_1(num_1, num_2):
    print(num_1 + num_2)


res_1 = add_num_1(10, 20)
print('函数返回值: ', res_1)
