# @Project ：Python_study
# @File    ：1.bug定位.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:05

def say_hello():
    print('[DEBUG]:say_hello')
    print('hello')


def say_goodbye():
    print('[DEBUG]:say_goodbye')
    print('hello')


if __name__ == '__main__':
    say_hello()
    say_goodbye()
