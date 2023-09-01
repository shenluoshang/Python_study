# @Project ：Python_study 
# @File    ：3.闭包的方式完成需求.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 21:12

def person(name):
    def say(message):
        print(f'{name}:{message}')

    return say


p1 = person('安娜')
p2 = person('双双')

p1('今天吃了吗？')
p2('吃了~')
p1('吃了啥？')
p2('一头羊~')
p1('为啥不给我吃？')
p2('我一个人刚刚好~')
p1('友谊的小船说翻就翻！')
p2('我会游泳~')

'''
当前闭包的核心是函数引用
    如何判断当前代码是闭包代码：
        1.达成函数关系
        2.内部函数可以使用外部函数的参数
        3.外部函数返回内部函数的引用
'''
