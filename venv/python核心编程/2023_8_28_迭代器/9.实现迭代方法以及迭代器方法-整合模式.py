# @Project ：Python_study 
# @File    ：9.实现迭代方法以及迭代器方法-整合模式.py
# @Author  ：魏洪志
# @Date    ：2023/8/28 21:28



from collections.abc import Iterator, Iterable


class MyList:
    def __init__(self):
        self.items = list()
        self.current = 0


    def add(self, value):
        self.items.append(value)

    def __iter__(self):
        # 返回一个迭代器对象
        return self

    def __next__(self):
        # 定义迭代的具体过程
        if self.current < len(self.items):
            item = self.items[self.current]
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
