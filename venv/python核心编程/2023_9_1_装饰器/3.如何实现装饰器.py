# @Project ：Python_study 
# @File    ：3.如何实现装饰器.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:12


def debug(func_obj):
    def wrapper():
        print(f'[debug]:{func_obj.__name__}')
        func_obj()

    return wrapper


def say_hello():
    print('hello')


func_obj = say_hello

func_obj = debug(func_obj)
func_obj()
