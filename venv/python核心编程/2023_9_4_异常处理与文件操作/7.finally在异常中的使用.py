# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午8:47
# @Author  : 顾安
# @File    : 7.finally在异常中的使用.py
# @Software: PyCharm


import pymysql


try:
    mysql_client = pymysql.connect(user='root', password='123', db='py_spider')
except:
    print('链接失败')
else:
    print('try代码块中的程序没有报错的情况下当前会被执行...')
finally:  # 一定会被执行的代码块
    print('无论代码是否报错, 当前代码一定会被执行...')
