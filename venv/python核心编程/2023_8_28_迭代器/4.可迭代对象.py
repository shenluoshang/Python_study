# @Project ：Python_study 
# @File    ：4.可迭代对象.py
# @Author  ：魏洪志
# @Date    ：2023/8/28 20:34

from collections.abc import Iterable

'''
一般可以使用for循环验证一个对象是否是一个可迭代对象

'''

int_data = 10
# for i in int_data:
#     pass


float_data = 3.15
# for i in float_data:
#     pass


bool_data = False
# for i in bool_data:
#     pass


print(isinstance(int_data,Iterable))
print(isinstance(float_data,Iterable))
print(isinstance(bool_data,Iterable))