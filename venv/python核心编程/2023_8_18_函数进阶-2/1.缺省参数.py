# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午8:01
# @Author  : 魏洪志
# @File    : 1.缺省参数.py
# @Software: PyCharm


def test_1(name, age=18):
    print(name, age)


test_1('双双', 20)  # 可以重新传入一个新的值覆盖原有默认的参数

test_1('安娜')


"""
数据库
    mysql
    redis
    mongodb
    
    1.python去控制数据库
        使用python去链接数据库
            链接数据库需要知道当前这个数据库所安装的计算机的ip地址以及数据库的运行端口
            
            
        3306
        6379
        17027
"""

# 缺省参数定义的位置必须在形式参数的后面
# def test_2(name='安娜', age):
#     pass



