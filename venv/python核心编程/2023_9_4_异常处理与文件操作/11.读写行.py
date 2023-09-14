# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午9:40
# @Author  : 顾安
# @File    : 11.读写行.py
# @Software: PyCharm


file_name = '测试文件.txt'
file_obj = open(file_name, 'a')


# result = file_obj.readlines()
# print(result)

data_list = ['\n你好', '\n很高兴认识你', '\n以后多多关照']
file_obj.writelines(data_list)

# 当大家用完文件对象之后记得关闭
file_obj.close()


