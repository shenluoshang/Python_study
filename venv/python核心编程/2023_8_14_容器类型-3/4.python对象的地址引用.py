# @Project ：Python_study 
# @File    ：4.python对象的地址引用.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 20:59

name = '顾安'
# 当前变量存储的是一个值的内存地址，而不是值本身
print(id(name))

info = {'name': '木木', 'age': 16}
print(id(info))


# 创建两个函数
def test_1():
    print('我是函数1')


def test_2():
    print('我是函数2')


print(id(test_1), id(test_2))


# 将函数2的内存地址赋值给test_1
test_1 = test_2
test_1()