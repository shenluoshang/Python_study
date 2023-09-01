# @Project ：Python_study 
# @File    ：9.类装饰器的实现.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:52

class Logging:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'[debug]:{self.func.__name__}')
        self.func(*args, **kwargs)


@Logging
def say(msg):
    print(msg)


say('你好')