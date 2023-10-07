# @Project ：Python_study 
# @File    ：3.使用面向对象的方式完成代码.py
# @Author  ：魏洪志
# @Date    ：2023/10/7 21:58

# 创建一个学生类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'姓名:{self.name},年龄:{self.age}')


p1 = Student('安娜', 20)
