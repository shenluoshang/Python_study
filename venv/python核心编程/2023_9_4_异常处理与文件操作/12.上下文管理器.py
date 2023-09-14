# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午9:46
# @Author  : 顾安
# @File    : 12.上下文管理器.py
# @Software: PyCharm


file_name = '测试文件.txt'

with open(file_name, 'r',encoding='utf-8') as file_obj:
    result = file_obj.read()
    print(result)
    # file_obj.close()


# class MyOpen:
#     def __init__(self):
#         self.file_obj = None
#
#     def __enter__(self):
#         self.file_obj = open(file_name)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file_obj.close()

