# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午9:34
# @Author  : 顾安
# @File    : 10.数据写入.py
# @Software: PyCharm


file_name = '/Users/poppies/Desktop/测试文件.txt'

# 如果指定的文件不存在 open会自动创建这个文件
# 会覆盖原有的数据
# 不想覆盖数据把读写模式改成 a
file_obj = open(file_name, 'w')
file_obj.write('下午一起去游泳...')
