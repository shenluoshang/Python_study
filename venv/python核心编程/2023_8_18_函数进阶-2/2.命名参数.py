# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午8:09
# @Author  : 魏洪志
# @File    : 2.命名参数.py
# @Software: PyCharm


def test(a, b):
    print(f'a={a}, b={b}')


test(11, 20)

test(b=20, a=11)  # 命名参数



