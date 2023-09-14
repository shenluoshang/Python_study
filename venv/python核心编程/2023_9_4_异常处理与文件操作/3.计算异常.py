# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午8:14
# @Author  : 顾安
# @File    : 3.计算异常.py
# @Software: PyCharm


def exp_exception(x, y):
    try:
        result = x / y
        print(result)
    except Exception as e:  # 当前位置的错误类型是可以省略的
        print('程序错误: ', e)


exp_exception(9, 0)
