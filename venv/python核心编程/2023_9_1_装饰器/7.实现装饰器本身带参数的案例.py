# @Project ：Python_study 
# @File    ：7.实现装饰器本身带参数的案例.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:33


'''
在DUBUG的过程中需要输出当前日志等级
'''


def level(le):
    def debug(func):
        def wrapper(*args, **kwargs):
            print(f'[debug]:{func.__name__}', le)
            func(*args, **kwargs)

        return wrapper

    return debug


@level('info')
def say(msg):
    print(msg)


if __name__ == '__main__':
    say('你好')
