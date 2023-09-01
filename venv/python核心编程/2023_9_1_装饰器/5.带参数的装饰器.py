# @Project ：Python_study 
# @File    ：5.带参数的装饰器.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:22


def debug(func):
    def wrapper(msg):
        # 因为被装饰的函数中有参数，所以需要在wrapper函数中添加形参以便调用被装饰的代码
        print(f'[DEBUG]:{func.__name__}')
        func(msg)

    return wrapper


@debug
def say(msg):
    print(f'信息内容：{msg}')


say('111')
