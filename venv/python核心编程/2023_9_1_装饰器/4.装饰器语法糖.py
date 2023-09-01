# @Project ：Python_study 
# @File    ：4.装饰器语法糖.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:19


def debug(func_obj):
    def wrapper():
        print(f'[debug]:{func_obj.__name__}')
        func_obj()

    return wrapper


@debug
def say_hello():
    print('hello')


say_hello()

'''
@debug 主要运行了三行代码：
    func_obj = say_hello
    func_obj = debug(func_obj)
    
    # 装饰器并没有执行第三个代码，当前第三个代码是在第21行执行的
    func_obj()
'''
