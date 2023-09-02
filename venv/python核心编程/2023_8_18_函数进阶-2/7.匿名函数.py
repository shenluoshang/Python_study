# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午9:16
# @Author  : 魏洪志
# @File    : 7.匿名函数.py
# @Software: PyCharm

"""
没有名字的函数
匿名函数只能被运行一次

匿名函数其实是一种表达式

lambda [可以在当前位置传递形参]: 你要返回的返回值
"""

# 没有形式参数的匿名函数
func_obj_1 = lambda: '这是一个返回值'
print(func_obj_1())

# 定义携带形式参数的匿名函数
func_obj_2 = lambda a, b: a + b
res = func_obj_2(1, 2)
print(res)

# 使用lambda完成元素排序
student_list = [
    {'name': '魏洪志', 'age': 20},
    {'name': '安娜', 'age': 18},
    {'name': '双双', 'age': 19}
]


def sort_by_age(stu_dict):
    return stu_dict['age']


sorted_student_list = sorted(student_list, key=sort_by_age)
print(sorted_student_list)

student_list.sort(key=lambda stu_dict: stu_dict['age'])
print(student_list)

