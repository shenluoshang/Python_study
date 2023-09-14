# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午8:21
# @Author  : 顾安
# @File    : 4.手动抛出异常.py
# @Software: PyCharm


try:
    raise NameError
    print(1)
except:
    print('代码异常')
