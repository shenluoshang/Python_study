# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 下午8:44
# @Author  : 魏洪志
# @File    : 5.函数返回值拆包.py
# @Software: PyCharm


def test_1():
    return 1, 2, 3


a, b, c = test_1()
print(a, b, c)

res = test_1()
print(res[0], res[1], res[2])


def test_2(a, b, c):
    print(a, b, c)


nums = [11, 22, 33]
test_2(nums[0], nums[1], nums[2])

test_2(*nums)  # 当前的*是可以进行拆包的, 在拆包之后会将当前的元素依次赋值给函数的参数


def test_3(name, gender, address):
    print(f'name: {name}, gender: {gender}, address: {address}')


info = {
    'name': '夏洛',
    'gender': '男',
    'address': '火星'
}

test_3(**info)



