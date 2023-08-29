# @Project ：Python_study 
# @File    ：8.实现迭代方法以及迭代器方法-分离模式.py
# @Author  ：魏洪志
# @Date    ：2023/8/28 21:10

from collections.abc import Iterator, Iterable


class MyList:
    def __init__(self):
        self.items = list()

    def add(self, value):
        self.items.append(value)

    def __iter__(self):
        # 返回一个迭代器对象
        return MyIterator(self)


class MyIterator:
    def __init__(self, my_list_obj):
        self.my_list_obj = my_list_obj
        # 定义一个计数器
        self.current = 0


    def __next__(self):
        # 定义迭代的具体过程
        if self.current < len(self.my_list_obj.items):
            item = self.my_list_obj.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration  #手动抛出异常

if __name__ == '__main__':
    my_list = MyList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)

    for item in my_list:
        print(item)
