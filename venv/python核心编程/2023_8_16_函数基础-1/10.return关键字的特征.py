# -*- coding: utf-8 -*-
# @Time    : 2023/8/16 下午9:03
# @Author  : 魏洪志
# @File    : 10.return关键字的特征.py
# @Software: PyCharm


# 函数遇到return关键字会自动退出
def run_function():
    print('函数启动...')
    return
    print('111')


run_function()


# return可以返回多个值
def get_info():
    num = 1
    name = '安娜'
    info = [{'gender': '女'}, {'age': 18}]
    return num, name, info


num, name, info = get_info()
print(num, name, info)


# 在函数中return只能有一个
def test_return():
    print('测试-1...')
    return
    print('测试-2...')
    return
    print('测试-3...')


test_return()

"""
总结:
    1.可以使用return将函数的结果返回给一个变量, 也可以直接去打印函数调用之后的结果
    2.函数在遇到return会终止函数运行
    3.return可以一次返回多个值, 并将多个值打包成一个元组
    4.函数中只能存在一个return
"""


def is_test(num_1, num_2):
    if num_1 > num_2:
        return 1
    else:
        return 2


res = is_test(9, 10)
print(res)
