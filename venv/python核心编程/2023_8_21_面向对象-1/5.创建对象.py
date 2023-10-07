# @Project ：Python_study 
# @File    ：5.创建对象.py
# @Author  ：魏洪志
# @Date    ：2023/10/7 22:19

class Dog:
    # 初始化方法
    def __init__(self, name):
        self.name = name

    def run(self, do):
        print(f'{self.name}正在{do}跑')


# 创建狗类的对象
jinmao = Dog('金毛')
jinmao.run('汪汪叫的')

hashiqi = Dog('哈士奇')
hashiqi.run('憨憨的')

