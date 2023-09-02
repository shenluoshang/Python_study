# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午8:13
# @Author  : 魏洪志
# @File    : 3.函数调用传参练习.py
# @Software: PyCharm


def test(a, b, c=100, d=200):
    print(f'a={a}, b={b}, c={c}, d={d}')


test(11, 22)
test(11, 22, 33)
test(11, 22, 33, 44)
test(11, 22, c=1, d=2)


# test(c=1, d=2)
# test(c=1, d=2, 11, 22)  # 命名参数需要再实参的后面




