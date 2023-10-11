# @Project ：Python_study
# @File    ：8.类中的self参数.py
# @Author  ：魏洪志
# @Date    ：2023/10/10 22:19

"""
python中的self是当前一个类的实例对象本身
    错的

    python中的self在编程规则下代表的是一个实例对象本身
        本质其实就是一个普通的参数而已
"""


class Dog:
    def __init__(self, name, age):
        # 当前的self是实例对象本身
        print(self)
        self.name = name
        self.age = age


"""
在做任何事情的时候不要太依赖权威
    勇于怀疑权威
"""

dog = Dog('萨摩耶', 2)
print(dog)


class Cat:
    def __init__(self, name, age):
        print(self)
        self.name = name
        self.age = age

    # 实例方法只能被实例对象调用
    def print_self(self):
        print(self)


cat = Cat('暹罗', 6)
# 其实self就是一个普通的形式参数而已 根据你所传递的对象进行接收
Cat.print_self('111')
cat.print_self()  # 自动将当前实例对象提交到self参数中

# 在python底层自动调用了一个方法: __class__将实例对象自动传参
cat.__class__.print_self(cat)

"""
1. 如何创建类
2. 如何创建对象
3. 如何创建实例属性
4. 如何访问实例属性
5. 如何创建实例对象
6. 如何使用实例对象
7. 如何在实例对象中获取实例属性
8. self的本质
"""
