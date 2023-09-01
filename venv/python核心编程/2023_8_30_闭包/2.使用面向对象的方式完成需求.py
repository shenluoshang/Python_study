# @Project ：Python_study 
# @File    ：2.使用面向对象的方式完成需求.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 21:08

class Person:
    def __init__(self, name):
        self.name = name

    def say(self, message):
        print(f'{self.name}:{message}')


p1 = Person('安娜')
p2 = Person('双双')

p1.say('今天吃了吗？')
p2.say('吃了~')
p1.say('吃了啥？')
p2.say('一头羊~')
p1.say('为啥不给我吃？')
p2.say('我一个人刚刚好~')
p1.say('友谊的小船说翻就翻！')
p2.say('我会游泳~')