# @Project ：Python_study 
# @File    ：10.带参数的类装饰器.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 21:02

class Logging:
    def __init__(self, level='info'):
        self.level = level

    def __call__(self, func):
        print(1)
        def wrapper(*args, **kwargs):
            print(f'[debug]:{func.__name__},level:{self.level}')
            func(*args, **kwargs)

        return wrapper


@Logging(level='error')
def say(msg):
    print(msg)


say('hello world')