# @Project ：Python_study 
# @File    ：2.对debug功能进行优化.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:08

import inspect


def debug():
    callable_name = inspect.stack()[1][3]
    print('[DEBUG]:enter {}()'.format(callable_name))


def say_hello():
    debug()
    print('hello')


def say_goodbye():
    debug()
    print('hello')

if __name__ == '__main__':
    say_hello()
    say_goodbye()