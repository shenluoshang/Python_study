# @Project ：Python_study 
# @File    ：7.自定义迭代方法以及定义迭代器方法.py
# @Author  ：魏洪志
# @Date    ：2023/8/28 21:00

from collections.abc import Iterable,Iterator


class MyList:
    def __init__(self):
        self.my_list = list()

    def add(self,item):
        self.my_list.append(item)

    def __iter__(self):
        # 要返回一个迭代器
        pass

    def __next__(self):
        pass

my_list = MyList()

my_list.add(1)
my_list.add(2)
my_list.add(3)

print(isinstance(my_list,Iterable))
print(isinstance(my_list,Iterator))


# iter_obj = iter(my_list)

for item in my_list:   # for 先判断是不是一个可迭代的，如果是 则达到for循环的第一个条件
    print(item)

'''
如果一个类的内部实现了__iter__方法，则这个类为可迭代对象
如果一个类的内部实现了__next__方法，则这个类为迭代器对象
'''

