# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午9:44
# @Author  : 魏洪志
# @File    : 8.递归函数.py
# @Software: PyCharm


"""
不建议去使用递归
    所谓的递归其实是使用循环的方式去调用自己
"""

# python对递归有次数限制: 997
# 最大递归深度
num = 10


def test():
    global num
    while num > 0:
        num -= 1
        test()


test()
