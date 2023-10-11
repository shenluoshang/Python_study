# @Project ：Python_study
# @File    ：6.类的实例属性.py
# @Author  ：魏洪志
# @Date    ：2023/10/10 22:19


# class Dog:
# 在实例化类之后需要自己手动调用设置实例属性的方法
# def set_attr(self, name, age):
#     self.name = name
#     self.age = age


# dog = Dog()
# dog.set_attr('哈士奇', 4)

"""
可以使用一个类的实例对象去访问一个类的实例属性
"""


# print(dog_1.name)
# print(dog_1.age)


class Dog:
    # 初始化方法
    # 类在实例化的过程中会自动调用初始化方法
    def __init__(self, name, age):
        # 设置实例属性
        self.name = name
        self.age = age


dog = Dog('金毛', 5)
print(dog.name)
print(dog.age)


# 动态设置实例属性
class Cat:
    pass


cat = Cat()
cat.name = '暹罗'
cat.age = 7
print(cat.name, cat.age)
