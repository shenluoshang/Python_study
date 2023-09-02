# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午8:47
# @Author  : 魏洪志
# @File    : 8.函数参数.py
# @Software: PyCharm

"""
在函数中参数是有分类的
    形式参数
    缺省参数
"""


# 形式参数
def add_1(a, b):
    print(a + b)


# 缺省参数
def add_2(a=5, b=11):
    print(a + b)


add_2(9, 20)

