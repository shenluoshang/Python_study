# @Project ：Python_study 
# @File    ：6.使用不定长参数创建装饰器.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:28

def debug(func):
    def wrapper(*args, **kwargs):
        # 因为被装饰的函数中有参数，所以需要在wrapper函数中添加形参以便调用被装饰的代码
        print(f'[DEBUG]:{func.__name__}')
        func(*args)
        print(kwargs)

    #     print 不支持打印**kwargs

    return wrapper


@debug
def say(*args, **kwargs):
    print(f'信息内容：{args}')


say('双双胖三斤', name='双双', age=18)
