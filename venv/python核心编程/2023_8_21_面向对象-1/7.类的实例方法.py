# @Project ：Python_study
# @File    ：7.类的实例方法.py
# @Author  ：魏洪志
# @Date    ：2023/10/10 22:19


class Dog:
    def __init__(self, name):
        self.name = name

    def print_dog_info(self):
        # 可以在一个实例方法中访问实例属性
        print(self.name)

    def run(self):
        print(f'{self.name}正在跑...')

    def eat(self, food):
        print(f'{self.name}正在吃{food}...')


dog = Dog('哈士奇')
dog.print_dog_info()
dog.run()
dog.eat('骨头')  # 当前所传入的参数是不是实例属性？
