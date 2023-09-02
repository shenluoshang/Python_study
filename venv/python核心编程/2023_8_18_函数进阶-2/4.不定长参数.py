# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午8:17
# @Author  : 魏洪志
# @File    : 4.不定长参数.py
# @Software: PyCharm


def test(a, b, *args, **kwargs):
    """
    :param a:
    :param b:
    :param args: 元组不定长, 可以接收多余的参数并打包成一个元组, 当然也可以不用传递任何参数
    :param kwargs: 字典不定长, 可以接收多余的缺省参数并打包成一个字典, 当然也可以不用传递任何参数
    :return:
    """
    # 在打印不定长参数的时候不要加 *
    print(f'a={a}, b={b}, *args={args}, **kwargs={kwargs}')


# 1.不给不定长参数传参
test(1, 2)

# 2.给元组不定长参数传参
test(1, 2, 3, 4)

# 3.给字典不定长传递参数
test(1, 2, name='安娜')

# 4.同时传递两个不定长
test(1, 2, 3, name='安娜')

info = {'name': '安娜', 'age': 20, 'gender': '女', 'address': '长沙'}
test(1, 2, info=info)

"""
args和kwargs
    args接收的是一个普通的参数对象
        
    kwargs接收的一定是一个命名参数
"""


# 因为元组不定长一定在字典不定长的前面
# def error_func(a, b, **kwargs, *args):
#     pass

def susses_func(a, b, c=10, *args, **kwargs):
    print(a, b, c, args, kwargs)


# 如果遇到参数必要复杂的函数, 想要把多余的参数传递给*args, 那么将多余的参数打包成一个元组进行传递
susses_func(1, 10, 90, [11, 22, 33], name='11')
