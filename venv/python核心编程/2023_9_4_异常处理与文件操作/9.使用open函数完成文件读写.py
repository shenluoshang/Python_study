# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午9:19
# @Author  : 顾安
# @File    : 9.使用open函数完成文件读写.py
# @Software: PyCharm


file_name = '测试文件.txt'

file_obj = open(file_name, encoding='utf-8')  # 返回一个对象, 文件对象
print(file_obj.read())

"""
大家在读取文件的时候可能会出现中文乱码的情况
    windows系统在编写文本文件的时候默认编码集是GBK
    在打开文件的时候指定编码集就可以了
    
read() 读到文件结尾
readline() 读一行
readlines() 读全本 返回一个列表
"""
