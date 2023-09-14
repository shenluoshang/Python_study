# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午9:56
# @Author  : 顾安
# @File    : 13.自定义读写类.py
# @Software: PyCharm


class OpenFile:
    # def __init__(self):
    #     # self.file_obj = None

    def __enter__(self):
        print(1)
        self.file_obj = open('测试文件.txt')  # 动态通过self创建了一个实例属性
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(2)
        self.file_obj.close()

    def my_read(self):
        print(self.file_obj.read())


with OpenFile() as file:
    file.my_read()
